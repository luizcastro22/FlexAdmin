from django.shortcuts import render, redirect
from .models import RegistroPonto
from .forms import RegistroPontoForm

def registrar_ponto(request):
    if request.method == 'POST':
        form = RegistroPontoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_ponto')
    else:
        form = RegistroPontoForm()
    
    registros = RegistroPonto.objects.all()
    return render(request, 'ponto/registrar_ponto.html', {'form': form, 'registros': registros})
