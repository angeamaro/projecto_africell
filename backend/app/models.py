from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from sqlalchemy.sql import func
from .connection import Base

class Client(Base):
    """
    Modelo ORM para a tabela 'users' no banco de dados.
    """
    __tablename__ = "clients"  

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(255), index=True, nullable=False)
    numero_bi = Column(String(50), unique=True, index=True, nullable=False)
    data_nascimento = Column(String(50))
    face_embedding = Column(LargeBinary, nullable=False) # Armazena o vetor de características faciais
    
    estado = Column(String(50), default="active") # O status é 'active' após o registro
    naturalidade = Column(String(100), index=True, nullable=False)
    provincia = Column(String(100), index=True, nullable=False) 
    genero = Column(String(20), index=True, nullable=False) # 'masculino' ou 'feminino'
    estado_civil = Column(String(50), index=True, nullable=False) # 'solteiro', 'casado', etc.
    residencia = Column(String(255), index=True, nullable=False) # Endereço de residência
    bi_validade = Column(String(50), nullable=False) # Data de validade do BI

    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_actualizacao = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, nome_completo='{self.nome_completo}', numero_bi='{self.numero_bi}')>"