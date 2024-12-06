from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from rolepermissions.decorators import has_role_decorator

from produtos.utils.pagination import make_pagination

from .forms import ProdutoForm, RegisterForm
from .models import Categoria, Pedido, Produto

PER_PAGE = 12

def index(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all().order_by('-id')
    page_obj, pagination = make_pagination(produtos, PER_PAGE, request)
    context = {"categorias": categorias, "produtos": page_obj, "pagination": pagination}

    return render(request, "index.html", context)


def produto_detalhes(request, id):
    produto = get_object_or_404(Produto, id=id)
    parcela = f"{produto.preco / 12:.2f}"
    preco = f"{produto.preco:.2f}"

    return render(
        request,
        "produto_detalhes.html",
        {
            "produto": produto,
            "parcela": parcela,
            "preco": preco,
        },
    )


@has_role_decorator("Admin")
def product_create(request):
    if request.method == "GET":
        form = ProdutoForm()
    elif request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto criado com sucesso!")
            return redirect("index")

    return render(request, "produto_form.html", {"form": form})


@has_role_decorator("Admin")
def product_update(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "GET":
        form = ProdutoForm(instance=produto)
    elif request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES,instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
        return redirect("produto_detalhes", id)

    return render(request, "produto_form.html", {"form": form})


@has_role_decorator("Admin")
def product_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, "Produto deletado com sucesso!")
    return redirect("index")


def product_search(request):
    products = Produto.objects.all()
    categorias = Categoria.objects.all()
    q = request.GET.get('q', '').strip()
    term = " ".join(q.split())
    search_page = True
    query = products.filter(
        Q(nome__icontains=term)
    )

    page_obj, pagination = make_pagination(query, PER_PAGE, request)

    return render(request, "index.html",
                   {
                       "produtos": page_obj,
                       "pagination": pagination,
                       "search_page": search_page,
                       "categorias": categorias,
                   }
                )


def category_filter(request):
    categorias = Categoria.objects.all()
    category_id = request.GET.get("categoria_id")
    category_products = Produto.objects.filter(
        categoria__id=category_id,
    )
    category_filter = True
    page_obj, pagination = make_pagination(category_products, PER_PAGE, request)

    return render(request, "index.html", 
                {
                    "produtos": page_obj,
                    "pagination": pagination,
                    "category_filter": category_filter,
                    "categorias": categorias,
                },
    )

def compra(request, id):
    try:
        produto = Produto.objects.get(id=id)
        produto.estoque -= 1
        produto.save()


        # Registrar o pedido
        pedido = Pedido.objects.create(
            cliente=request.user,
            produto=produto,
            valor=produto.preco,
        )

        pedido.save()
        messages.success(request, "Compra realizada com sucesso!")

    except Exception:
        messages.error(request, "Erro ao realizar a compra!")

    return redirect("produto_detalhes", id)


def user_register(request):
    if request.method == "GET":
        form = RegisterForm()
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Obtem os dados enviados no form
            first_name = form.data.get("first_name")
            last_name = form.data.get("last_name")
            username = form.data.get("username")
            email = form.data.get("email")
            password = form.data.get("password")

            # Registra o Usuário atribuindo o mesmo ao grupo 'Client' criado com rolepermissions.
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
            )
            user.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect("login")

    return render(request, "user_form.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha incorretos!")
    return render(
        request,
        "login.html",
    )


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')
