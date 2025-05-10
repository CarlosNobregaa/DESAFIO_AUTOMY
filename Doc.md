# Documentação - Desafio Automy

## Dados Pessoais

* **Nome:** Carlos Wagner Nóbrega Andriola
* **CPF:** 089.044.063-82
* **Email:** cwna829@gmail.com
* **Número:** 85997177586

---

## Instruções de Uso

1. Clone este repositório para sua máquina local:

   git clone https://github.com/CarlosNobregaa/DESAFIO_AUTOMY.git
   cd repositorio

2. Instale as dependências do projeto backend:

   cd src/backend
   pip install -r requirements.txt

3. Execute o backend localmente:

   uvicorn main:app --reload

4. **Certifique-se de que o CORS esteja configurado no `main.py`:**

   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:3000"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

5. Instale as dependências do frontend:

   cd ../../frontend
   npm install

6. Execute o frontend:

   npm start

7. Acesse a aplicação no navegador:

   http://localhost:3000

8. Insira um e-mail válido (como `john.doe@gmail.com`) e clique em "Consultar".
   As informações de baterias agendadas serão exibidas na tela.


## Estrutura do Projeto

* **/src/backend**: Contém o código backend, incluindo o arquivo `main.py` que gerencia as rotas da API.
* **/src/utils**: Contém utilitários como funções para separar baterias e montar a mensagem.
* **/services**: Contém integração com a API externa para buscar as baterias.
* **/src/frontend**: Contém a interface do usuário feita em React, com integração ao backend.

---

## Como Funciona

1. **Autenticação:** A aplicação usa um token JWT para se autenticar na API externa.
2. **Consulta de Dados:** O frontend envia o e-mail para o backend, que consulta a API externa para buscar as baterias.
3. **Lógica de Negócio:** As baterias são separadas em "futuras" e "passadas". A mensagem é montada com base nos dados.
4. **Resposta:** O frontend exibe a mensagem e as baterias diretamente na interface, sem necessidade de recarregar a página.


## Tecnologias Utilizadas

* **Python** (FastAPI)
* **React** (JavaScript)
* **Axios** (para requisições HTTP)
* **JWT Authentication** (para acessar a API externa)
* **CORS Middleware** (para comunicação entre frontend e backend)
