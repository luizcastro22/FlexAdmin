from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class RegistroPonto(models.Model):
    FUNCIONARIO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('intervalo', 'Intervalo'),
    )

    funcionario = models.ForeignKey('contrib.Funcionario', on_delete=models.DO_NOTHING, null= True)
    tipo = models.CharField(max_length=10, choices=FUNCIONARIO_CHOICES)
    data_hora = models.DateTimeField(default=timezone.now)

    