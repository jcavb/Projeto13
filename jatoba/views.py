from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Tarefa
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

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

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email já cadastrado.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                login(request, user)

                return redirect('protegida')
        else:
            messages.error(request, 'As senhas não coincidem.')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('protegida') 
        else:
            messages.error(request, 'Email ou senha inválidos.')
    return render(request, 'login.html')

@login_required
def pagina_protegida(request):
    return render(request, 'protegida.html')



