from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="products/covers/%Y/%m/%d/", blank=True, default="")

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.FloatField()
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.cliente}"

    