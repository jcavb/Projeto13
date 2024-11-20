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
        return render(request, 'visualizar_fert.html', {'fertilizante': fertilizantes})

def delete_fertilizante_view(request, id):
    ferti = get_object_or_404(Fertilizante, id=id)

    if request.method == 'POST':
        ferti.delete()  
        messages.success(request, 'Fetilizante excluído com sucesso!')
        return redirect('controle:visualizar_fert')  

    return render(request, 'confirmar_exclusao.html', {'fertilizante': ferti})
    
class AddSemente(View):
    def get (self, request):
        return render(request, 'semente.html')
    
    def post(self, request):
        sementes = request.POST.get("sementes")
        urlImagem = request.POST.get("imagem")

        controle = Semente(
            semente = sementes,
            imagem = urlImagem
        )

        controle.save()

        return redirect('controle:vizualisar_sem')

class VerSemente(View):
    def get (self, request):
        nome = Semente.objects.all()
        return render(request, 'visualizar_sem.html', {'semente': nome})

def delete_semente_view(request, id):
    sement = get_object_or_404(Semente, id=id)

    if request.method == 'POST':
        sement.delete()  
        messages.success(request, 'Sentente excluída com sucesso!')
        return redirect('controle:semente')  

    return render(request, 'confirmar_exclusao.html', {'semente': sement})