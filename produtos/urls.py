from django.urls import path

from produtos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/criar/', views.product_create, name='product_create'),
    path('produtos/atualizar/<int:id>/', views.product_update, name='product_update'),
    path('produtos/deletar/<int:id>/', views.product_delete, name='product_delete'),
    path('usuario/registrar/', views.user_register, name='user_register'),
]