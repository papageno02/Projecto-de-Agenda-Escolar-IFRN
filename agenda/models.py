
from django.db import models


class Turma(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da turma"
    )
    disciplina = models.CharField(
        max_length=100,
        verbose_name="Disciplina"
    )
    periodo = models.CharField(
        max_length=30,
        verbose_name="Período letivo"
    )
    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição"
    )
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.disciplina}"

    class Meta:
        ordering = ["nome"]
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Evento(models.Model):
    class TipoEvento(models.TextChoices):
        COMPROMISSO = "compromisso", "Compromisso geral"
        PROVA = "prova", "Prova"
        TRABALHO = "trabalho", "Trabalho avaliativo"
        REPOSICAO = "reposicao", "Reposição"

    titulo = models.CharField(
        max_length=150,
        verbose_name="Título"
    )
    tipo = models.CharField(
        max_length=20,
        choices=TipoEvento.choices,
        default=TipoEvento.COMPROMISSO,
        verbose_name="Tipo de evento"
    )
    data = models.DateField(verbose_name="Data")
    horario_inicio = models.TimeField(
        verbose_name="Horário de início"
    )
    horario_fim = models.TimeField(
        verbose_name="Horário de término"
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="eventos",
        verbose_name="Turma"
    )
    local = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Local"
    )
    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição ou observações"
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.data}"

    class Meta:
        ordering = ["data", "horario_inicio"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
