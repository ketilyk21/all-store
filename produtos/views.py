from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProdutoForm

from .models import Categoria, Produto


def index(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    context = {"categorias": categorias, "produtos": produtos}
    return render(request, "index.html", context)


def product_create(request):
    if request.method == "GET":
        form = ProdutoForm()
    elif request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "produto_form.html", {"form": form})


def product_update(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "GET":
        form = ProdutoForm(instance=produto)
    elif request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
        return redirect("index")

    return render(request, "produto_form.html", {"form": form})


def product_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("index")


def user_register(request):
    return render(request, "user_form.html")


def user_login(request):
    return render(request, "user_form.html")


def user_logout(request): ...
