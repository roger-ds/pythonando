from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        primeiro_nome = request.POST.get("primeiro_nome")
        ultimo_nome = request.POST.get("ultimo_nome")
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        email = request.POST.get("email")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not senha == confirmar_senha:
            messages.add_message(
                request, constants.ERROR, "As senhas não coincidem"
            )
            return redirect("/usuarios/cadastro")

        if len(senha) < 3:
            messages.add_message(
                request,
                constants.ERROR,
                "A senha deve ter pelo menos 3 caracteres",
            )
            return redirect("/usuarios/cadastro")

        try:
            User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
        except:
            messages.add_message(
                request, constants.ERROR, "Erro interno do sistema"
            )
            return redirect("/usuarios/cadastro")

        messages.add_message(
            request, constants.SUCCESS, "Usuário cadastrado com sucesso!"
        )
        return redirect("/usuarios/cadastro")


def logar(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.add_message(
                request, constants.ERROR, "Usuário ou senha inválidos"
            )
            return redirect("/usuarios/login")
