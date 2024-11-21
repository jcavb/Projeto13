from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View
from .models import Fertilizante, Semente

class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    
class AddFertilizante(View):
    def get (self, request):
        return render(request, 'fertilizante.html')
    
    def post(self, request):
        nome_fertilizantes = request.POST.get("nome")
        urlImagem = request.POST.get("imagem")

        Fertilizante.objects.create(
            fertilizante = nome_fertilizantes,
            imagem = urlImagem
        )

        return redirect('controle:visualizar_fert')

class VerFertilizante(View):
    def get (self, request):
        fertilizantes = Fertilizante.objects.all()
        return render(request, 'visualizar_fert.html', {'fertilizantes': fertilizantes})

def delete_fertilizante_view(request, id):
    ferti = get_object_or_404(Fertilizante, id=id)

    if request.method == 'POST':
        ferti.delete()  
        messages.success(request, 'Fetilizante excluído com sucesso!')
        return redirect('controle:visualizar_fert')  

    return render(request, 'delete_fertilizante.html', {'fertilizante': ferti})
    
class AddSemente(View):
    def get (self, request):
        return render(request, 'semente.html')
    
    def post(self, request):
        nome_sementes = request.POST.get("nome")
        urlImagem = request.POST.get("imagem")

        Semente.objects.create(
            semente = nome_sementes,
            imagem = urlImagem
        )

        return redirect('controle:visualizar_sem')

class VerSemente(View):
    def get (self, request):
        sementes = Semente.objects.all()
        return render(request, 'visualizar_sem.html', {'sementes': sementes})

def delete_semente_view(request, id):
    seme = get_object_or_404(Semente, id=id)

    if request.method == 'POST':
        seme.delete()  
        messages.success(request, 'Semente excluída com sucesso!')
        return redirect('controle:visualizar_sem')  

    return render(request, 'delete_semente.html', {'semente': seme})