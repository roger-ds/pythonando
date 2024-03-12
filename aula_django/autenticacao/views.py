from django.shortcuts import render
from django.http import HttpResponse
import json


def cadastro(request):
    print(request.GET)
    if request.method == "GET":
        nome = request.GET.get("nome")
        return render(request, "cadastro/index.html", {"nome": nome})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        return HttpResponse(json.dumps({"nome": nome, "email": email}))
