
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Turma, Evento
from .forms import EventoForm


def index(request):
    return render(request, "agenda/dashboard.html")


def listar_turmas(request):
    turmas = Turma.objects.all()
    return render(
        request,
        "agenda/turmas.html",
        {"turmas": turmas}
    )


def criar_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Evento cadastrado com sucesso!"
            )
            return redirect("agenda:meus_compromissos")
    else:
        form = EventoForm()

    return render(
        request,
        "agenda/evento_form.html",
        {"form": form}
    )


def meus_compromissos(request):
    eventos = Evento.objects.all()
    return render(
        request,
        "agenda/meus_compromissos.html",
        {"eventos": eventos}
    )


def avaliacoes(request):
    eventos = Evento.objects.filter(
        tipo__in=["prova", "trabalho", "reposicao"]
    )
    return render(
        request,
        "agenda/avaliacoes.html",
        {"eventos": eventos}
    )
