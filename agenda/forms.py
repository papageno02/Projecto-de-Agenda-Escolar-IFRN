
from django import forms
from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            "titulo",
            "tipo",
            "data",
            "horario_inicio",
            "horario_fim",
            "turma",
            "local",
            "descricao",
        ]

        labels = {
            "titulo": "Título do evento",
            "tipo": "Tipo de evento",
            "data": "Data",
            "horario_inicio": "Horário de início",
            "horario_fim": "Horário de término",
            "turma": "Turma relacionada",
            "local": "Local",
            "descricao": "Descrição ou observações",
        }

        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Ex.: Reunião pedagógica",
            }),
            "data": forms.DateInput(attrs={
                "type": "date",
            }),
            "horario_inicio": forms.TimeInput(attrs={
                "type": "time",
            }),
            "horario_fim": forms.TimeInput(attrs={
                "type": "time",
            }),
            "local": forms.TextInput(attrs={
                "placeholder": "Ex.: Sala 05",
            }),
            "descricao": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Informações adicionais...",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        tipo = cleaned_data.get("tipo")
        turma = cleaned_data.get("turma")
        inicio = cleaned_data.get("horario_inicio")
        fim = cleaned_data.get("horario_fim")

        if tipo in ["prova", "trabalho", "reposicao"] and not turma:
            self.add_error(
                "turma",
                "Selecione uma turma para cadastrar uma avaliação."
            )

        if inicio and fim and fim <= inicio:
            self.add_error(
                "horario_fim",
                "O horário de término deve ser posterior ao início."
            )

        return cleaned_data
