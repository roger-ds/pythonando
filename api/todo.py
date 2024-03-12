from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date


class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]


lista = []

app = FastAPI()

@app.post("/inserir")
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return {"status": "sucesso"}
    except: 
        return {"status": "erro"}


@app.post("/listar")
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))


@app.get("/lista_index/{idx}")
def lista_index(idx: int):
    try:
        return lista[idx]
    except:
        return {"status": "erro"}



@app.post("/altera_status")
def inserir(idx: int):
    try:
        lista[idx].realizada = not lista[idx].realizada
        return {"status": "sucesso"}
    except: 
        return {"status": "erro"}



@app.post("/excluir")
def inserir(idx: int):
    try:
        del lista[idx]
        return {"status": "sucesso"}
    except: 
        return {"status": "erro"}