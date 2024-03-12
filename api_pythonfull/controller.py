from fastapi import FastAPI
from models import session, Pessoa, Tokens
from secrets import token_hex
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from hashlib import sha256


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/cadastro")
def cadastro(usuario: str, email: str, senha: str):
    if len(senha) < 6:
        return {"erro": 1}
    senha = sha256(senha.encode()).hexdigest()
    user_exist = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()
    if user_exist:
        return {"erro": 2}
    try:
        novo_usuario = Pessoa(usuario=usuario, email=email, senha=senha)
        session.add(novo_usuario)
        session.commit()
        return {"erro": 0}
    except Exception as e:
        return {"erro": 3, "erro_db": e}
    

if __name__ == "__main__":
    uvicorn.run("controller:app", port=5000, reload=True, access_log=False)

    # No terminal: uvicorn main:app --reload