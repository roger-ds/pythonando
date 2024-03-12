from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensagem": "home"}


@app.get("/cadastro")
def root():
    return {"mensagem": "cadastro"}


@app.get("/login")
def root():
    x = 0
    for i in range(10):
        x += i
    return {"mensagem": "cadastro", "valor": x}