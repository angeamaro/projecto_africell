from pydantic import BaseModel, Field
from typing import Optional

class BiDataExtracted(BaseModel):
    """Esquema para os dados extraídos do BI."""
    full_name: Optional[str] = Field(None, description="Nome completo extraído do BI.")
    bi_number: Optional[str] = Field(None, description="Número do Bilhete de Identidade.")
    birth_date: Optional[str] = Field(None, description="Data de nascimento extraída (DD/MM/AAAA).")
    # Adicionar outros campos que possam ser extraídos no futuro
    naturalidade: Optional[str] = None
    provincia: Optional[str] = None
    genero: Optional[str] = None
    estado_civil: Optional[str] = None
    residencia: Optional[str] = None
    bi_validade: Optional[str] = None
    numero_telefone: Optional[str] = None # Se puder ser lido do BI ou fornecido

class UploadBiResponse(BaseModel):
    """Resposta após o upload da imagem do BI."""
    message: str
    session_id: str = Field(..., description="ID da sessão temporária para o processo de cadastro.")
    bi_data: BiDataExtracted

class LiveCaptureResponse(BaseModel):
    """Resposta após a captura da imagem ao vivo e comparação facial."""
    message: str
    distance: float = Field(..., description="Distância de similaridade entre as faces.")

class VerifySmsResponse(BaseModel):
    """Resposta após a verificação do código SMS e finalização do cadastro."""
    message: str
    user_id: int = Field(..., description="ID do usuário recém-registrado no banco de dados.")

class UserCreate(BaseModel):
    """Esquema para criar um novo usuário (usado internamente ou por rotas admin)."""
    nome_completo: str
    numero_bi: str
    data_nascimento: str
    # face_embedding: bytes # Não será recebido diretamente via API, mas sim gerado
    estado: Optional[str] = "active"
    naturalidade: str
    provincia: str
    genero: str
    estado_civil: str
    residencia: str
    bi_validade: str
    numero_telefone: str