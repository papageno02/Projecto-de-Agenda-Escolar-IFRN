from django.shortcuts import render
from .models import Turma

def index(request):
    return render(request,'agenda/dashboard.html')

def listar_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'agenda/turmas.html', {'turmas': turmas})

def criar_evento(request):
    return render(request, 'agenda/evento_form.html')
