from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


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
