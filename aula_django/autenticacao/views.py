from django.shortcuts import render
from django.http import HttpResponse
import json
from hashlib import sha256
from .models import Pessoa


def cadastro(request):
    print(request.GET)
    if request.method == "GET":
        nome = request.GET.get("nome")
        return render(request, "cadastro/index.html", {"nome": nome})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = sha256(request.POST.get("senha").encode()).hexdigest()
        pessoa = Pessoa(nome=nome, email=email, senha=senha)
        pessoa.save()
        return HttpResponse(json.dumps({"nome": nome, 
                                        "email": email, 
                                        "senha": senha}))


def listar(request):
    # pessoas = (Pessoa.objects.filter(senha="96020064") | Pessoa.objects.filter(nome="Lu")).exclude(senha="12345678")
    excluir = Pessoa.objects.filter(nome="Lu").filter(senha="12345678")[0]
    excluir.delete()
    
    pessoas = Pessoa.objects.all()
    return render(request, "listar/pessoas.html", {"pessoas": pessoas})