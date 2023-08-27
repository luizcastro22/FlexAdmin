from django.db import models
from contrib.models import Funcionario

# Create your models here.

class Gerente(models.Model):
    funcionario = models.OneToOneField(Funcionario,on_delete=models.CASCADE,null=True)
    
