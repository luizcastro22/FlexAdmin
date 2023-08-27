from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import FuncionarioCadastroForm

def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioCadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            senha = form.cleaned_data['senha']

            # Criação do nome de usuário
            username = f"{nome}"
            while User.objects.filter(username=username).exists():
                username += '_1'  # Adicionar sufixo incremental até encontrar um nome único

            # Criação do usuário
            user = User.objects.create_user(username=username, password=senha)

            # Criação do funcionário
            funcionario = form.save(commit=False)
            funcionario.user = user
            funcionario.save()

            return redirect('/')  # Redirecione para onde desejar após o cadastro
    else:
        form = FuncionarioCadastroForm()

    return render(request, 'cadastro.html', {'form': form})