from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RegistroPonto
from .forms import RegistroPontoForm

@login_required
def registrar_ponto(request):
    funcionario = request.user.funcionario  # Assumindo que você tem um campo 'funcionario' na sua model de usuário
    
    if request.method == 'POST':
        form = RegistroPontoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.funcionario = funcionario
            registro.save()
            return redirect('registrar_ponto')
    else:
        form = RegistroPontoForm()

    registros = RegistroPonto.objects.filter(funcionario=funcionario)
    return render(request, 'ponto/registrar_ponto.html', {'form': form, 'registros': registros})
