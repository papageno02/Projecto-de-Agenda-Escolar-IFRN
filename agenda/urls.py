from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.index, name='index'),
    path("dashboard/", views.index, name="dashboard"),
    path("turmas/", views.listar_turmas, name="listar_turmas"),
    path("eventos/novo/", views.criar_evento, name="criar_evento"),

]