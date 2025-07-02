import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do ficheiro .env
load_dotenv()

# Conecta ao banco de dados MySQL
# Certifique-se de que o 'mysqlclient' está instalado para a parte 'mysql+mysqlclient'
DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Cria a engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria a classe Base para os modelos
Base = declarative_base()

# Cria a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Função para obter a sessão do banco de dados (usada nas rotas da API)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Cria as tabelas no banco de dados com base nos modelos definidos."""
    Base.metadata.create_all(bind=engine)