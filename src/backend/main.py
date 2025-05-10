from fastapi import FastAPI, Query
from services.automy_api import buscar_baterias_por_email
from utils.bateria_utils import separar_baterias, montar_mensagem
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ou ["*"] para permitir tudo (menos seguro)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def baterias(email: str = Query(...)):
    dados = await buscar_baterias_por_email(email)
    baterias_futuras, baterias_passadas = separar_baterias(dados)
    mensagem = montar_mensagem(email, baterias_futuras, baterias_passadas)
    return mensagem
