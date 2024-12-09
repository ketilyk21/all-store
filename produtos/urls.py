from django.urls import path

from produtos import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "produtos/detalhes/<int:id>/", views.produto_detalhes, name="produto_detalhes"
    ),
    path("produtos/search/", views.product_search, name="search"),
    path("produtos/criar/", views.product_create, name="product_create"),
    path("produtos/comprar/<int:id>/", views.compra, name="produto_comprar"),
    path("produtos/atualizar/<int:id>/", views.product_update, name="product_update"),
    path("produtos/deletar/<int:id>/", views.product_delete, name="product_delete"),
    path("category/filter/", views.category_filter, name="category_filter"),
    path("usuario/registrar/", views.user_register, name="register"),
    path("usuario/login/", views.user_login, name="login"),
    path("usuario/logout/", views.user_logout, name="logout"),
    path("pedidos/gerenciar/", views.listar_pedidos, name="listar_pedidos"),
    path("pedidos/admin/deletar/<int:id>/", views.pedidos_deletar, name="pedidos_deletar"),
    path("pedidos/", views.meus_pedidos, name="meus_pedidos"),
    path("pedidos/deletar/<int:id>/", views.deletar_meus_pedidos, name="deletar_meus_pedidos"),
]
