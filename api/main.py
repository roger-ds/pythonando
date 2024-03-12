from fastapi import FastAPI
from models import session, Pessoa, Tokens
from secrets import token_hex


app = FastAPI()


@app.post("/cadastro")
def cadastro(nome: str, user: str, senha: str):
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()
    if not usuario:
        p = Pessoa(nome=nome, usuario=user, senha=senha)
        session.add(p)
        session.commit()
        return {"status": "sucesso"}
    else: 
        return {"status": "Usuário já cadastrado"}


@app.post("/login")
def login(user: str, senha: str):
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()
    if not usuario:
        return {"status": "Usuario inexistente"}
    
    while True:
        token = token_hex(50)
        token_existe = session.query(Tokens).filter_by(token=token).all()
        if not token_existe:
            token_id_pessoa_existe = session.query(Tokens).filter_by(id_pessoa=usuario[0].id).all()
            if not token_id_pessoa_existe:
               novo_token = Tokens(id_pessoa=usuario[0].id, token=token)
               session.add(novo_token)
            else:
               token_id_pessoa_existe[0].token = token

        session.commit()
        break
    return token
