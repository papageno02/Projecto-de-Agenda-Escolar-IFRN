
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import LoginForm, CadastroForm

User = get_user_model()

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect("index")

    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"].strip().lower()
        senha = form.cleaned_data["senha"]

        usuario = authenticate(
            request,
            username=email,
            password=senha,
        )

        if usuario is not None:
            login(request, usuario)
            return redirect("index")

        messages.error(
            request,
            "E-mail ou senha inválidos."
        )

    return render(
        request,
        "contas/login.html",
        {"form": form},
    )

def cadastro_usuario(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    form = CadastroForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"]
        senha = form.cleaned_data["senha"]

        User.objects.create_user(
            username=email,
            email=email,
            password=senha,
        )

        messages.success(
            request,
            "Cadastro realizado! Agora você pode entrar."
        )

        return redirect("login")

    return render(
        request,
        "contas/cadastro.html",
        {"form": form},
    )

def inicio(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "contas/inicio.html")

def sair_usuario(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")