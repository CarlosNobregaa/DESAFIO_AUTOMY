import pytest
from fastapi.testclient import TestClient
from main import app
from utils.bateria_utils import separar_baterias, montar_mensagem

client = TestClient(app)

def test_baterias():
    response = client.get("/?email=john.doe@gmail.com")
    assert response.status_code == 200
    assert "mensagem" in response.json()

def test_separar_baterias():
    dados_mock = [
        {"data_agendamento": "10/05/2025", "horario_agendamento": "20h", "email": "john.doe@gmail.com", "nome": "John Doe", "qtde_pessoas": "25"},
        {"data_agendamento": "18/04/2025", "horario_agendamento": "19h", "email": "john.doe@gmail.com", "nome": "John Doe", "qtde_pessoas": "8"},
    ]
    
    baterias_futuras, baterias_passadas = separar_baterias(dados_mock)
    
    assert len(baterias_futuras) == 1 
    assert len(baterias_passadas) == 1 
    assert baterias_futuras[0]["data"] == "10/05/2025" 
    assert baterias_passadas[0]["data"] == "18/04/2025" 

def test_montar_mensagem():
    baterias_futuras = [{"data": "10/05/2025", "horario": "20h", "nome": "John Doe", "qtde_pessoas": "25"}]
    baterias_passadas = [{"data": "18/04/2025", "horario": "19h", "nome": "John Doe", "qtde_pessoas": "8"}]

    mensagem = montar_mensagem("john.doe@gmail.com", baterias_futuras, baterias_passadas)

    assert "Olá! Encontramos" in mensagem["mensagem"]
