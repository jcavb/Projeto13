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
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Atividade 
from django.conf import settings
import requests
import datetime


@login_required
def gerar_relatorio_pdf(request):
    # Criação do response para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_atividades.pdf"'

    # Criação do PDF
    p = canvas.Canvas(response)
    p.setTitle("Relatório de Atividades CAIS")

    # Título do documento
    p.drawString(100, 800, "Relatório de Atividades Realizadas no CAIS")

    # Buscando atividades realizadas no banco de dados
    atividades = Atividade.objects.filter(realizada=True)  # Filtre conforme sua lógica de negócio
    
    # Listando as atividades no PDF
    y = 750
    for atividade in atividades:
        p.drawString(100, y, f"Atividade: {atividade.tipo} - Descrição: {atividade.descricao} - Data: {atividade.data_realizacao}")
        y -= 20
        if y < 100:
            p.showPage()
            y = 750

    # Finalizando o PDF
    p.showPage()
    p.save()
    return response



@login_required
def city_characteristics(request):
    api_key = settings.OPENWEATHERMAP_API_KEY
    city = 'Carpina'
    
    # Recebe a data selecionada pelo usuário, ou usa a data atual se não houver seleção
    selected_date = request.GET.get('date', datetime.date.today().isoformat())

    # Realiza a chamada para a API do OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Inicializa a lista para armazenar os dados de previsão do dia selecionado
    weather_data = []
    if response.status_code == 200:
        for forecast in data['list']:
            forecast_date = datetime.datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
            
            # Verifica se a data da previsão corresponde à data selecionada
            if forecast_date == selected_date:
                weather_data.append({
                    'date': forecast_date,
                    'temperature': forecast['main']['temp'],
                    'humidity': forecast['main']['humidity'],
                    'description': forecast['weather'][0]['description'],
                })
        
        if not weather_data:
            error_message = f'Não há dados de previsão para a data selecionada: {selected_date}.'
            weather_data = [{'date': 'Erro', 'description': error_message}]
    else:
        error_message = data.get('message', 'Erro ao obter dados de previsão.')
        weather_data = [{'date': 'Erro', 'description': error_message}]

    return render(request, 'city_characteristics.html', {'weather_data': weather_data, 'city': city, 'selected_date': selected_date})




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

            return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Por favor, preencha todos os campos.'})

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

