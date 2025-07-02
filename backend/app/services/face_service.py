import numpy as np
import cv2
from deepface import DeepFace
import os

# Define o caminho para o modelo de detecção de face (opcional, pode ser 'opencv', 'ssd', 'mtcnn', 'retinaface' etc.)
DETECTOR_BACKEND = 'mtcnn' # mtcnn é robusto para rostos de baixa resolução

def get_face_embedding(image_path: str):
    """
    Extrai o embedding (vetor de características) de um rosto de uma imagem usando DeepFace.
    
    Args:
        image_path (str): Caminho para o arquivo de imagem.
        
    Returns:
        numpy.ndarray: O embedding facial, ou None se nenhum rosto for encontrado.
    """
    try:
        embeddings = DeepFace.represent(
            img_path=image_path,
            model_name="ArcFace", # Mude aqui para "ArcFace" ou "Facenet"
            enforce_detection=True,
            detector_backend=DETECTOR_BACKEND
        )
        
        # DeepFace.represent retorna uma lista de dicionários (uma para cada rosto)
        if embeddings:
            return np.array(embeddings[0]["embedding"])
        else:
            return None # Nenhum rosto encontrado
            
    except Exception as e:
        print(f"Erro ao obter embedding com DeepFace: {e}")
        return None

def compare_faces(bi_image_path: str, live_image_path: str):
    """
    Compara dois rostos de imagens usando DeepFace e retorna a distância de similaridade.
    Menor distância indica maior similaridade.
    
    Args:
        bi_image_path (str): Caminho para a imagem do BI.
        live_image_path (str): Caminho para a imagem capturada ao vivo.
        
    Returns:
        float: Distância de similaridade, ou uma distância alta (ex: 1.0) se a comparação falhar.
    """
    try:
        # DeepFace.verify retorna um dicionário com 'verified', 'distance', etc.
        result = DeepFace.verify(
            img1_path=bi_image_path,
            img2_path=live_image_path,
            model_name="ArcFace", # Usar o mesmo modelo para comparação
            detector_backend=DETECTOR_BACKEND,
            enforce_detection=True
        )
        return result["distance"]
    except Exception as e:
        print(f"Erro ao comparar faces com DeepFace: {e}")
        return 1.0 # Retorna uma distância alta em caso de erro

def get_embeddings_from_folder(folder_path: str):
    """
    Obtém embeddings de todos os rostos em imagens dentro de uma pasta.
    
    Args:
        folder_path (str): Caminho da pasta com as imagens.
        
    Returns:
        dict: Um dicionário com o nome do ficheiro e o embedding.
    """
    embeddings_dict = {}
    
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não foi encontrada.")
        return embeddings_dict
        
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            embedding = get_face_embedding(image_path)
            if embedding is not None:
                embeddings_dict[filename] = embedding
                
    return embeddings_dict
        
def extract_face_from_image(image_path: str):
    """
    Detecta e recorta a área do rosto de uma imagem.
    DeepFace já faz isso internamente, mas podemos criar uma função para extrair a face separadamente.
    """
    try:
        # DeepFace.extract_faces retorna a face detectada
        faces = DeepFace.extract_faces(
            img_path=image_path,
            detector_backend=DETECTOR_BACKEND,
            enforce_detection=True
        )
        
        if faces:
            # Retorna a face recortada como uma imagem OpenCV (BGR)
            face_pixels = faces[0]["face"] # A DeepFace já retorna a imagem do rosto
            return face_pixels
        else:
            return None # Nenhum rosto detectado
            
    except Exception as e:
        print(f"Erro ao extrair rosto da imagem: {e}")
        return None