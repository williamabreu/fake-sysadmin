"""
Definição de rotas do CRUD do Atendente.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-cliente/', views.create_client, name='create_client'),
    path('listar-clientes/', views.list_all_clients, name='list_all_clients'),
]
