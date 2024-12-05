from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ("nome", "descricao", "preco", "categoria", "imagem", "estoque")
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "estoque": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "imagem": forms.FileInput(attrs={"class": "form-control"}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if len(nome) < 3:
            raise ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
        return nome

    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao")
        if len(descricao) < 10:
            raise ValidationError("A descrição deve ter pelo menos 10 caracteres.")
        return descricao

    def clean_preco(self):
        preco = self.cleaned_data.get("preco")
        if preco <= 0:
            raise ValidationError("O preço deve ser maior que zero.")
        return preco


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirme sua senha", "class": "form-control"}
        ),
        label="Confirmação de senha",
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Ex.: John", "class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Ex.: Doe", "class": "form-control"}
            ),
            "username": forms.TextInput(
                attrs={"placeholder": "Seu usuário", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Seu e-mail", "class": "form-control"}
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Sua senha", "class": "form-control"}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está registrado.")
        return email

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError("As senhas não correspondem.")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nome de usuário já está em uso.")
        if len(username) < 3:
            raise ValidationError("O nome de usuário deve ter pelo menos 3 caracteres.")
        return username
