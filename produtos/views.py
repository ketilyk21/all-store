from django.shortcuts import redirect, render

from .models import Categoria, Produto


def index(request):
    categorias = Categoria.objects.all() 
    produtos = Produto.objects.all() 
    context = {'categorias': categorias, 'produtos': produtos}
    return render(request, "index.html", context)


def product_create(request):
    return render(request, "produto_form.html")


def product_update(request):
    return render(request, "produto_form.html")


def product_delete(request):
    return redirect("index")


def user_register(request):
    return render(request, "user_form.html")


def user_login(request):
    return render(request, "user_form.html")


def user_logout(request): ...
 