from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

@login_required
def pagina_protegida(request):
    return render(request, 'protegida.html')

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

