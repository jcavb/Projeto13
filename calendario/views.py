# calendario/views.py
from django.shortcuts import render

def calendario(request):
    return render(request, 'calendario.html')  # Renderiza o HTML do calendário
