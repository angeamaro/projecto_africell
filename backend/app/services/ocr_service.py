import cv2
import pytesseract
import numpy as np
import re
import os
from .face_service import extract_face_from_image

# Define a pasta para uploads temporários
TEMP_UPLOADS_DIR = "temp_uploads"
os.makedirs(TEMP_UPLOADS_DIR, exist_ok=True) # Cria a pasta se ela não existir

# Configura o caminho do executável do Tesseract se necessário
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def save_image_from_upload(upload_file_content, filename):
    """Salva o conteúdo de um arquivo de upload em um diretório temporário."""
    file_path = os.path.join(TEMP_UPLOADS_DIR, filename)
    with open(file_path, "wb") as buffer:
        buffer.write(upload_file_content)
    return file_path

def parse_bi_text(text: str):
    """
    Analisa o texto extraído do BI para encontrar campos relevantes usando expressões regulares.
    Adapte as expressões regulares (regex) ao layout específico do BI angolano, se necessário.
    """
    data = {}
    
    full_name_match = re.search(r'Nome Completo:\s*(.*)', text, re.IGNORECASE)
    if full_name_match:
        data['full_name'] = full_name_match.group(1).strip()
        
    bi_number_match = re.search(r'Bilhete de Identidade N[º°]:?\s*([\w\d]+)', text, re.IGNORECASE)
    if bi_number_match:
        data['bi_number'] = bi_number_match.group(1).strip()
        
    birth_date_match = re.search(r'Data de Nascimento:\s*(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
    if birth_date_match:
        data['birth_date'] = birth_date_match.group(1).strip()
    
    # Adicionar mais regex para outros campos do BI, se necessário
    # Ex: naturalidade, província, género, estado civil, residência, validade
    
    return data

def extract_data_and_face_from_bi(image_path: str):
    """
    Extrai dados de texto e o rosto de uma imagem do Bilhete de Identidade a partir de um caminho de ficheiro.
    
    Args:
        image_path (str): Caminho para o arquivo de imagem no disco.
        
    Returns:
        tuple: Um dicionário com os dados extraídos e a imagem do rosto.
    """
    try:
        # --- Passo 1: Extração de texto usando OCR ---
        img_cv = cv2.imread(image_path)
        
        if img_cv is None:
            print(f"Erro: Não foi possível carregar a imagem em {image_path}")
            return {}, None

        gray_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        
        # Aplicar limiarização e outras operações de pré-processamento para melhorar o OCR
        _, thresh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Opcional: Remover ruído ou dilatar/erosionar
        # kernel = np.ones((1,1), np.uint8)
        # thresh_img = cv2.dilate(thresh_img, kernel, iterations=1)
        # thresh_img = cv2.erode(thresh_img, kernel, iterations=1)

        text = pytesseract.image_to_string(thresh_img, lang='por') # 'por' para português
        
        bi_data = parse_bi_text(text)
        
        # --- Passo 2: Extração do rosto ---
        face_image_np = extract_face_from_image(image_path) # Retorna um numpy array (BGR)
        
        return bi_data, face_image_np
        
    except Exception as e:
        print(f"Erro ao extrair dados e rosto do BI: {e}")
        return {}, None