from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar-plano/', views.create_plan, name='create_plan'),
    path('modificar-plano/<int:id>/', views.update_plan, name='update_plan'),
    # path('listar-planos/', views.index, name='listar-planos'),
]