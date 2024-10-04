from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Tarefa
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('protegida') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()

    if request.method == 'POST':
        tarefa_id = request.POST.get('tarefa_id')
        try:
            tarefa = Tarefa.objects.get(id=tarefa_id)
            tarefa.concluida = not tarefa.concluida
            tarefa.save()
            return JsonResponse({'success': True})
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'error': 'Tarefa não encontrada'}, status=404)
    
    return render(request, 'tarefas.html', {'tarefas': tarefas})

@login_required
def pagina_protegida(request):
    return render(request, 'protegida.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


