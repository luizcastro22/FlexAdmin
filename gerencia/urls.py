from django.urls import path
from . import views

urlpatterns = [
    path('alterar_registro/<int:registro_id>/', views.alterar_registro_ponto, name='alterar_registros'),
    path('cadastrar_gerente/',views.cadastrar_gerente, name="cadastro_gerente"),
    path('', views.selecionar_funcionario, name = 'selecionar_funcionario')
]