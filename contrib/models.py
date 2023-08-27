from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Funcionario(models.Model):
    class Meta:
        db_table = "Funcionario"
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="", null=True)
    nome = models.CharField(max_length=25,default="")
    sobrenome = models.CharField(max_length=25,default="")



    def __str__(self):
        return self.nome

    