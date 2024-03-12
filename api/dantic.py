from fastapi import FastAPI
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nome: str
    senha: str


app = FastAPI()


lista = [
    Usuario(id=1, nome="roger", senha="fisxal"),
    Usuario(id=2, nome="ana", senha="med122"),
    Usuario(id=3, nome="helen", senha="333333"),
]


@app.post("/usuario")
def main(usuario: Usuario):
    lista.append(usuario)
    return "Usuario cadastrado"



@app.get("/usuario_listar")
def main():
    return lista