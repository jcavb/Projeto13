from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Tarefa
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cultura
from django.utils.timezone import now 
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model, login

def home(request):
    return render(request, 'home.html')

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()

    if request.method == 'POST':
        # Verifica se é um pedido de atualização de tarefa ou de criação de nova tarefa
        if 'tarefa_id' in request.POST:
            tarefa_id = request.POST.get('tarefa_id')
            try:
                tarefa = Tarefa.objects.get(id=tarefa_id)
                tarefa.concluida = not tarefa.concluida
                tarefa.save()
                return JsonResponse({'success': True})
            except ObjectDoesNotExist:
                return JsonResponse({'success': False, 'error': 'Tarefa não encontrada'}, status=404)
        
        # Adicionando nova tarefa
        elif 'nome_tarefa' in request.POST and 'categoria_tarefa' in request.POST:
            nome_tarefa = request.POST.get('nome_tarefa')
            categoria_tarefa = request.POST.get('categoria_tarefa')
            nova_tarefa = Tarefa(
                nome=nome_tarefa, 
                categoria=categoria_tarefa, 
                data_ultima_acao=now(),  # Define a data atual como data_ultima_acao
                concluida=False
            )
            nova_tarefa.save()
            return redirect('tarefas')  # Redireciona de volta para a lista de tarefas

    return render(request, 'tarefas.html', {'tarefas': tarefas})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password2:
            if password1 != password2:
                return render(request, 'signup.html', {'error': 'As senhas não coincidem.'})

            if get_user_model().objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Nome de usuário já existe.'})

            if get_user_model().objects.filter(email=email).exists():
                return render(request, 'signup.html', {'error': 'Email já cadastrado.'})

            # Criar usuário
            user = get_user_model().objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Autenticar e logar o usuário, especificando o EmailBackend
            backend = 'jatoba.backends.EmailBackend'  # Atualize com o caminho correto do seu EmailBackend
            login(request, user, backend=backend)

            return redirect('protegida')
        else:
            return render(request, 'signup.html', {'error': 'Por favor, preencha todos os campos.'})

    return render(request, 'protegida.html')

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

def buscar_cultura(request):
    query = request.GET.get('q')
    resultados = None
    if query:
        resultados = Cultura.objects.filter(nome__icontains=query)
    return render(request, 'infos.html', {'resultados': resultados})

def banana_infos(request):
    return render(request, 'culturas/banana.html')

def abacate_infos(request):
    return render(request, 'culturas/abacate.html')

def brocolis_infos(request):
    return render(request, 'culturas/brocolis.html')

def cenoura_infos(request):
    return render(request, 'culturas/cenoura.html')

def couve_infos(request):
    return render(request, 'culturas/couve.html')

def macaxeira_infos(request):
    return render(request, 'culturas/macaxeira.html')

def rucula_infos(request):
    return render(request, 'culturas/rucula.html')

def tomate_infos(request):
    return render(request, 'culturas/tomate.html')

