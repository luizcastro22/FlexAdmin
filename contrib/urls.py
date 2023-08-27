from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_funcionario, name='cadastrar_funcionario'),
]