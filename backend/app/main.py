from fastapi import FastAPI
from app.connection import create_tables
from app.routes import register # Importa as rotas de registro

app = FastAPI(
    title="Africel - Cadastro Biométrico",
    description="API para o sistema de cadastro seguro de números telefônicos com reconhecimento facial e verificação por BI.",
    version="1.0.0"
)

# Evento de startup para criar as tabelas no banco de dados
@app.on_event("startup")
def on_startup():
    create_tables()
    print("Tabelas do banco de dados verificadas/criadas.")

# Incluir as rotas da API
app.include_router(register.router, prefix="/api/v1/register", tags=["Cadastro"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["Usuários"]) # Exemplo para rotas de usuário