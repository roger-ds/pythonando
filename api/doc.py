from fastapi import FastAPI


app = FastAPI()

usuarios = [(1, "caio", "minhasenha"), (2, "roger", "1234")]


@app.post("/test")
def main(nome: str):
    for i in usuarios:
        if i[1] == nome:
            return i

    return "Não existe esse usuário"