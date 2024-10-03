
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o novo usuário
            login(request, user)  # Faz login automático após o cadastro
            return redirect('home')  # Redireciona para a página inicial ou dashboard
    else:
        form = UserCreationForm()  # Exibe o formulário vazio
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render

