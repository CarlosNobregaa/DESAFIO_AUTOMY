import httpx
import os
from dotenv import load_dotenv

load_dotenv()

async def buscar_baterias_por_email(email: str):
    async with httpx.AsyncClient() as client:
        login_resp = await client.post(
            "https://appsaccess.automy.com.br/login",
            json={"username": os.getenv("AUTOMY_USER"), "password": os.getenv("AUTOMY_PASS")}
        )
        token = login_resp.json().get("token")

        query = f"""
            SELECT * FROM desafio.cadastro_baterias_desafio
            WHERE email = '{email}'
        """

        consulta_resp = await client.post(
            "https://appsaccess.automy.com.br/api/api/desafio/custom/do/query",
            headers={"Authorization": f"Bearer {token}"},
            json={"query": query.strip(), "db": "desafio"}
        )

        return consulta_resp.json()
