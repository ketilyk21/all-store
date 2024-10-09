from django import forms
from .models import Produto
from django.contrib.auth.models import User


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ("nome", "descricao", "preco", "categoria", "imagem")

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "imagem": forms.FileInput(attrs={"class": "form-control"}),
        }


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirme sua senha", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        )

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
