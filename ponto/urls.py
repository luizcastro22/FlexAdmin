from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_ponto, name='registrar_ponto'),
]