
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "placeholder": "Digite seu e-mail",
            "autocomplete": "email",
        }),
    )

    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Digite sua senha",
            "autocomplete": "current-password",
        }),
    )

class CadastroForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "placeholder": "Digite seu e-mail",
            "autocomplete": "email",
        }),
    )

    senha = forms.CharField(
        label="Senha",
        min_length=8,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Crie uma senha com pelo menos 8 caracteres",
            "autocomplete": "new-password",
        }),
    )

    confirmar_senha = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Digite a senha novamente",
            "autocomplete": "new-password",
        }),
    )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Este e-mail já está cadastrado."
            )

        return email

    def clean(self):
        dados = super().clean()
        senha = dados.get("senha")
        confirmar_senha = dados.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error(
                "confirmar_senha",
                "As senhas não são iguais."
            )

        return dados