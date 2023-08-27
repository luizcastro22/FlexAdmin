from contrib.models import Funcionario
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import GerenteCadastroForm, AlterarRegistroPontoForm, SelecionarFuncionarioForm
from ponto.models import RegistroPonto

def cadastrar_gerente(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        gerente_form = GerenteCadastroForm(request.POST)

        if user_form.is_valid() and gerente_form.is_valid():
            user = user_form.save()
            gerente = gerente_form.save(commit=False)
            gerente.user = user
            gerente.save()
            return redirect('/')

    else:
        user_form = UserCreationForm()
        gerente_form = GerenteCadastroForm()

    return render(request, 'gerencia/cadastro_gerente.html', {'user_form': user_form, 'gerente_form': gerente_form})


 

# @permission_required('app.change_pontos')  # Use a permissão correta aqui
def alterar_registro_ponto(request, registro_id):
    registro = RegistroPonto.objects.get(pk=registro_id)
    
    if request.method == 'POST':
        form = AlterarRegistroPontoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('selecionar_funcionario')  # Redirecione para onde desejar após a edição
    else:
        form = AlterarRegistroPontoForm(instance=registro)
    
    return render(request, 'gerencia/alterar_registro_ponto.html', {'form': form})

def selecionar_funcionario(request):
    if request.method == 'POST':
        form = SelecionarFuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.cleaned_data['funcionario']
            registros = RegistroPonto.objects.filter(funcionario=funcionario)
            return render(request, 'gerencia/listar_registros.html', {'registros': registros, 'funcionario': funcionario})
    else:
        form = SelecionarFuncionarioForm()

    return render(request, 'gerencia/selecionar_funcionario.html', {'form': form})