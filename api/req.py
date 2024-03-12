import requests


retorno = requests.post("http://127.0.0.1:8000/test/?nome=caio")#, params={"nome": "roger"})

print(retorno.json())
