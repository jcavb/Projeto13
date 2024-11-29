import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    # Caso a localidade não esteja disponível, defina para a localidade padrão
    locale.setlocale(locale.LC_TIME, '')
    # Ou você pode optar por usar uma biblioteca como Babel para internacionalização

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Tarefa
from django.core.exceptions import ObjectDoesNotExist  # type: ignore
from django.http import JsonResponse  # type: ignore
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cultura, Fertilizante, Semente, Rotacoes, Culturas
from django.utils.timezone import now  # type: ignore
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404
from django.views import View  # type: ignore
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import calendar

@login_required
def adicionar_observacao(request):
    if request.method == 'POST':
        # Obtém a observação ou define um valor padrão
        observacao = request.POST.get('observacao', 'Nenhuma observação fornecida')

        # Configura o response para download do PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="observacao.pdf"'

        # Cria o canvas para o PDF
        p = canvas.Canvas(response)
        p.setTitle("Relatório com Observação")

        # Adiciona cabeçalho no PDF
        p.drawString(100, 800, f"Relatório do Usuário: {request.user.username}")
        p.drawString(100, 780, "----------------------------------------")

        # Adiciona a observação
        p.drawString(100, 750, "Observação:")
        p.drawString(100, 730, observacao)

        # Finaliza o PDF
        p.showPage()
        p.save()

        return response

    # Caso GET, renderiza o formulário
    return render(request, 'adicionar_observacao.html')

@login_required
def calendario(request):
    mes = int(request.GET.get('mes', datetime.now().month))
    ano = int(request.GET.get('ano', datetime.now().year))

    _, dias_no_mes = calendar.monthrange(ano, mes)
    primeiro_dia_semana = calendar.monthrange(ano, mes)[0]  # Índice do primeiro dia da semana (0=Segunda)

    # Consulta tarefas para o mês e ano atuais
    tarefas = Tarefa.objects.filter(dia__year=ano, dia__month=mes)

    # Gera os dias do mês com as tarefas associadas
    dias = []
    for dia_num in range(1, dias_no_mes + 1):
        tarefas_do_dia = tarefas.filter(dia__day=dia_num)
        dias.append({'dia': dia_num, 'tarefas': tarefas_do_dia})

    # Prepara células vazias para o template (dias anteriores ao início do mês)
    celulas_vazias = list(range(primeiro_dia_semana))

    return render(request, 'calendario.html', {
        'dias': dias,
        'celulas_vazias': celulas_vazias,
        'mes': mes,
        'ano': ano,
        'nome_mes': calendar.month_name[mes],
        'anterior_mes': (mes - 1) if mes > 1 else 12,
        'anterior_ano': (ano - 1) if mes == 1 else ano,
        'proximo_mes': (mes + 1) if mes < 12 else 1,
        'proximo_ano': (ano + 1) if mes == 12 else ano,
    })

@login_required
def adicionar_tarefa(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')
        if descricao and dia and mes and ano:
            try:
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                data = datetime(ano, mes, dia).date()
                tarefa = Tarefa.objects.create(dia=data, descricao=descricao)
                return JsonResponse({'id': tarefa.id, 'descricao': tarefa.descricao})
            except ValueError:
                return JsonResponse({'error': 'Data inválida'}, status=400)
        else:
            return JsonResponse({'error': 'Dados inválidos'}, status=400)
    else:
        return JsonResponse({'error': 'Método inválido'}, status=400)

@login_required
def excluir_tarefa(request, tarefa_id):
    if request.method == 'POST':
        try:
            tarefa = Tarefa.objects.get(id=tarefa_id)
            tarefa.delete()
            return JsonResponse({'success': True})
        except Tarefa.DoesNotExist:
            return JsonResponse({'error': 'Tarefa não encontrada'}, status=404)
    return JsonResponse({'error': 'Método inválido'}, status=400)

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

def home(request):
    return render(request, 'home.html')

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

@login_required
def pagina_protegida(request):
    user_name = request.user.first_name or request.user.username
    return render(request, 'protegida.html', {'user_name': user_name})

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

class AddFertilizante(View):
    def get(self, request):
        return render(request, 'fertilizante.html')

    def post(self, request):
        nome_fertilizantes = request.POST.get("nome")
        urlImagem = request.POST.get("imagem")

        if not nome_fertilizantes or not urlImagem:
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'fertilizante.html')

        Fertilizante.objects.create(
            fertilizante=nome_fertilizantes,
            imagem=urlImagem
        )
        messages.success(request, "Fertilizante adicionado com sucesso!")
        return redirect('jatoba:menu')

class VerFertilizante(View):
    def get(self, request):
        fertilizantes = Fertilizante.objects.all()
        return render(request, 'visualizar_fert.html', {'fertilizantes': fertilizantes})

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

def delete_fertilizante_view(request, id):
    ferti = get_object_or_404(Fertilizante, id=id)

    if request.method == 'POST':
        ferti.delete()
        return JsonResponse({'status': 'success', 'message': 'Fertilizante excluído com sucesso!'})

    return JsonResponse({'status': 'error', 'message': 'Requisição inválida'}, status=400)

class AddSemente(View):
    def get(self, request):
        return render(request, 'semente.html')

    def post(self, request):
        nome_sementes = request.POST.get("nome")
        urlImagem = request.POST.get("imagem")

        if not nome_sementes or not urlImagem:
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'semente.html')

        Semente.objects.create(
            semente=nome_sementes,
            imagem=urlImagem
        )
        messages.success(request, "Semente adicionada com sucesso!")
        return redirect('jatoba:menu')

class VerSemente(View):
    def get(self, request):
        sementes = Semente.objects.all()
        return render(request, 'visualizar_sem.html', {'sementes': sementes})

def delete_semente_view(request, id):
    if request.method == 'POST':
        try:
            seme = get_object_or_404(Semente, id=id)
            seme.delete()
            return JsonResponse({'status': 'success', 'message': 'Semente excluída com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Erro ao excluir a semente.', 'details': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Método inválido. Apenas POST é permitido.'}, status=400)

class Rotacao(View):
    def get(self, request):
        cultura_rotacoes = Culturas.objects.all()

        # Converte o ID da cultura selecionada para inteiro, caso exista
        rotacao_cultura_id = request.GET.get('cultura')
        rotacao_cultura_id = int(rotacao_cultura_id) if rotacao_cultura_id else None

        rotacao = None
        if rotacao_cultura_id:
            rotacao = Rotacoes.objects.filter(cultura_id=rotacao_cultura_id)

        context = {
            'cultura_rotacoes': cultura_rotacoes,
            'rotacao': rotacao,
            'rotacao_cultura_id': rotacao_cultura_id,
        }

        return render(request, 'rotacao.html', context)

    def post(self, request):
        rotacao_cultura_id = request.POST.get('cultura')
        rotacao_id = request.POST.get('rotacao')

        # Redireciona para outra página ou implementa lógica adicional
        return redirect('rotacao')

@login_required
def menu_view(request):
    fertilizantes = Fertilizante.objects.all()
    sementes = Semente.objects.all()

    context = {
        'fertilizantes': fertilizantes,
        'sementes': sementes,
    }
    return render(request, 'menu.html', context)

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Substitua 'login' pela URL da página de login
