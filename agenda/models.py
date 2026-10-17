
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
    criada_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nome} - {self.disciplina}"

    class Meta:
        ordering = ["nome"]
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"