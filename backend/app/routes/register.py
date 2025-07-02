from fastapi import APIRouter, File, UploadFile, HTTPException, Depends, Form
from sqlalchemy.orm import Session
import os
import shutil
import numpy as np
import uuid
import cv2 # Para salvar o numpy array do rosto se DeepFace.represent não aceitar direto

from app.services.ocr_service import extract_data_and_face_from_bi, save_image_from_upload
from app.services.face_service import get_face_embedding, compare_faces
from app.services.sms_service import generate_sms_code, send_sms
from app.connection import get_db
from app.models import User
from app.schemas import UploadBiResponse, LiveCaptureResponse, VerifySmsResponse, BiDataExtracted, UserCreate

router = APIRouter()

# Limiar de similaridade (pode ser movido para uma configuração global se preferir)
SIMILARITY_THRESHOLD = 0.5

# Dicionário temporário para armazenar dados de sessão (AVISO: Não usar em produção sem um cache persistente como Redis!)
# Em produção, usaria um sistema de cache (Redis) ou um banco de dados para gerenciar sessões
session_store = {}

@router.post("/upload_bi/", response_model=UploadBiResponse)
async def upload_bi_image(bi_image: UploadFile = File(...)):
    """
    Endpoint para fazer upload da imagem do Bilhete de Identidade (BI).
    Extrai dados de texto e o embedding facial do BI.
    """
    if not bi_image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O ficheiro deve ser uma imagem (PNG, JPG, JPEG).")

    session_id = str(uuid.uuid4())
    # Garante que a pasta temp_uploads existe
    os.makedirs(os.path.join(os.getcwd(), "temp_uploads"), exist_ok=True)
    
    temp_bi_path = os.path.join("temp_uploads", f"{session_id}_bi_{bi_image.filename}")

    # Salva a imagem temporariamente
    with open(temp_bi_path, "wb") as buffer:
        shutil.copyfileobj(bi_image.file, buffer)

    # Extrai dados e rosto do BI usando o serviço de OCR
    bi_data_dict, face_image_np = extract_data_and_face_from_bi(temp_bi_path)

    if not bi_data_dict:
        os.remove(temp_bi_path)
        raise HTTPException(status_code=400, detail="Não foi possível extrair dados do BI. Verifique a qualidade da imagem e o layout.")
    
    if face_image_np is None:
        os.remove(temp_bi_path)
        raise HTTPException(status_code=400, detail="Nenhum rosto foi detectado na imagem do BI. Certifique-se de que o rosto está claro e visível.")

    # Converte o rosto recortado (numpy array) para um arquivo temporário para gerar o embedding
    temp_face_bi_path = os.path.join("temp_uploads", f"{session_id}_face_bi_cropped.jpg")
    cv2.imwrite(temp_face_bi_path, face_image_np)

    bi_embedding = get_face_embedding(temp_face_bi_path)
    
    # Limpa o arquivo temporário do rosto recortado
    os.remove(temp_face_bi_path)

    if bi_embedding is None:
        os.remove(temp_bi_path) # Limpa o arquivo original do BI também
        raise HTTPException(status_code=500, detail="Erro ao gerar o embedding facial do BI.")

    # Converte o dicionário para o modelo Pydantic
    bi_data_parsed = BiDataExtracted(**bi_data_dict)

    # Armazena os dados na sessão temporária
    session_store[session_id] = {
        "bi_data": bi_data_parsed.model_dump(), # Salva como dict para fácil serialização se session_store fosse Redis
        "bi_embedding": bi_embedding.tobytes(), # Armazenar o numpy array como bytes
        "temp_bi_path": temp_bi_path # Manter o caminho para o arquivo original do BI para comparação direta
    }

    return UploadBiResponse(
        message="Dados do BI extraídos com sucesso. Prossiga para a captura ao vivo.",
        session_id=session_id,
        bi_data=bi_data_parsed
    )

@router.post("/capture_live/", response_model=LiveCaptureResponse)
async def capture_live_image(
    session_id: str = Form(..., description="ID da sessão obtido no passo anterior."),
    live_image: UploadFile = File(...)
):
    """
    Endpoint para fazer upload da imagem capturada ao vivo.
    Compara o rosto capturado com o rosto extraído do BI.
    Se houver correspondência, simula o envio de um código SMS.
    """
    session_data = session_store.get(session_id)
    if not session_data:
        raise HTTPException(status_code=404, detail="Sessão não encontrada ou expirou. Por favor, reinicie o processo de cadastro.")

    if not live_image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O ficheiro deve ser uma imagem (PNG, JPG, JPEG).")

    temp_live_path = os.path.join("temp_uploads", f"{session_id}_live_{live_image.filename}")
    with open(temp_live_path, "wb") as buffer:
        shutil.copyfileobj(live_image.file, buffer)

    # Verifica se o temp_bi_path ainda existe antes de tentar usar
    if not os.path.exists(session_data["temp_bi_path"]):
        # Isso pode acontecer se a imagem original do BI for removida cedo demais ou se o servidor reiniciar
        os.remove(temp_live_path)
        raise HTTPException(status_code=500, detail="Imagem original do BI não encontrada para comparação. Por favor, reinicie o processo.")

    # Compara as faces usando os caminhos dos arquivos
    # compare_faces() já cuida da extração de embedding internamente se usar caminhos
    distance = compare_faces(session_data["temp_bi_path"], temp_live_path)

    # Limpa os arquivos temporários após a comparação
    os.remove(temp_live_path)
    os.remove(session_data["temp_bi_path"]) # Remove o arquivo original do BI

    if distance > SIMILARITY_THRESHOLD:
        raise HTTPException(status_code=400, detail=f"Correspondência facial falhou. Distância: {distance:.4f} (limiar: {SIMILARITY_THRESHOLD}). Tente novamente com uma foto mais clara.")

    # Se a correspondência for bem-sucedida, gera e "envia" o código SMS
    verification_code = generate_sms_code()
    # Pega o número de telefone do BI ou de um campo de formulário adicional
    phone_number_from_bi = session_data["bi_data"].get("numero_telefone")
    
    # Você precisaria que o frontend enviasse o número de telefone para o qual enviar o SMS,
    # ou que o OCR fosse capaz de extraí-lo do BI. Por enquanto, é um placeholder.
    if not phone_number_from_bi:
        # Por exemplo, para testes, ou se o número será inserido manualmente no frontend
        # Ou um número fictício para simulação
        phone_number_from_bi = os.getenv("TEST_PHONE_NUMBER", "244923456789") # Exemplo de fallback

    sms_message = f"Seu codigo de verificacao Africel e: {verification_code}"
    
    # Chama o serviço de SMS (assíncrono)
    sms_sent = await send_sms(phone_number_from_bi, sms_message)
    
    if not sms_sent:
        raise HTTPException(status_code=500, detail="Erro ao enviar o código SMS. Por favor, tente novamente.")

    # Armazena o código de verificação e o número de telefone no session_store
    session_data["verification_code"] = verification_code
    session_data["phone_number_for_sms"] = phone_number_from_bi # Armazena o número para o qual o SMS foi enviado
    session_store[session_id] = session_data

    return LiveCaptureResponse(
        message="Verificação facial bem-sucedida. Um código de verificação foi enviado por SMS.",
        distance=distance
    )

@router.post("/verify_sms/", response_model=VerifySmsResponse)
async def verify_sms_and_register(
    session_id: str = Form(..., description="ID da sessão."),
    code: str = Form(..., description="Código de verificação recebido por SMS."),
    # Parâmetros adicionais que o frontend pode enviar para completar o registro
    naturalidade: str = Form(...),
    provincia: str = Form(...),
    genero: str = Form(...),
    estado_civil: str = Form(...),
    residencia: str = Form(...),
    bi_validade: str = Form(...),
    numero_telefone: str = Form(..., description="Número de telefone a ser cadastrado e usado para o SMS."),
    db: Session = Depends(get_db)
):
    """
    Endpoint para verificar o código SMS e finalizar o cadastro do usuário.
    """
    session_data = session_store.get(session_id)
    if not session_data:
        raise HTTPException(status_code=404, detail="Sessão não encontrada ou expirou.")

    # Verifica se o código SMS é válido
    if code != session_data.get("verification_code"):
        raise HTTPException(status_code=400, detail="Código de verificação inválido. Tente novamente.")

    # Valida o número de telefone fornecido pelo usuário no frontend (pode ser o mesmo do BI ou um novo)
    if not numero_telefone: # Validação básica
         raise HTTPException(status_code=400, detail="Número de telefone é obrigatório.")

    # Verifica se já existe um usuário com o mesmo número de BI ou telefone
    existing_user_bi = db.query(User).filter(User.numero_bi == session_data["bi_data"]["bi_number"]).first()
    if existing_user_bi:
        # Se for um recadastro para o mesmo BI, podemos atualizar ou negar
        # Por simplicidade, vamos negar para evitar duplicatas para o mesmo BI_NUMBER
        raise HTTPException(status_code=409, detail="Já existe um cadastro para este número de BI.")

    existing_user_phone = db.query(User).filter(User.numero_telefone == numero_telefone).first()
    if existing_user_phone:
        raise HTTPException(status_code=409, detail="Este número de telefone já está cadastrado.")

    # Cria o novo registro de usuário no banco de dados
    new_user = User(
        nome_completo=session_data["bi_data"]["full_name"],
        numero_bi=session_data["bi_data"]["bi_number"],
        data_nascimento=session_data["bi_data"]["birth_date"],
        face_embedding=session_data["bi_embedding"], # O embedding já está em bytes
        estado="active", # Define o estado como ativo após o registro bem-sucedido
        naturalidade=naturalidade,
        provincia=provincia,
        genero=genero,
        estado_civil=estado_civil,
        residencia=residencia,
        bi_validade=bi_validade,
        numero_telefone=numero_telefone
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        del session_store[session_id] # Limpa a sessão após o registro bem-sucedido
        return VerifySmsResponse(
            message="Cadastro realizado com sucesso!",
            user_id=new_user.id
        )
    except Exception as e:
        db.rollback()
        # Logar o erro completo para depuração
        print(f"Erro ao salvar usuário no banco de dados: {e}")
        raise HTTPException(status_code=500, detail=f"Erro interno ao finalizar o cadastro. Detalhes: {e}")