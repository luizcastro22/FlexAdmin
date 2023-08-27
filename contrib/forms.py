from django import forms
from django.contrib.auth.models import User
from .models import Funcionario

class FuncionarioCadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())  # Novo campo

    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'senha', 'confirmar_senha']  # Adicione 'confirmar_senha'
    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")
        
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem. Por favor, insira as senhas novamente.")
