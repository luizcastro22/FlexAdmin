from django import forms
from .models import Gerente
from ponto.models import RegistroPonto
from contrib.models import Funcionario

class GerenteCadastroForm(forms.ModelForm):
    cargo = forms.CharField(max_length=50)

    class Meta:
        model = Gerente
        fields = ['cargo']

class SelecionarFuncionarioForm(forms.Form):
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all())

class AlterarRegistroPontoForm(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        fields = ['funcionario','tipo', 'data_hora']  # Defina os campos que podem ser alterados
