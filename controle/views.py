from django.shortcuts import render, redirect
from django.views import View
from .models import Fertilizante, Semente

class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    
class AddFertilizante(View):
    def get (self, request):
        return render(request, 'fertilizante.html')
    
    def post(self, request):
        fertilizantes = request.POST.get("fertilizantes")
        urlImagem = request.POST.get("imagem")

        controle = Fertilizante(
            fertilizante = fertilizantes,
            imagem = urlImagem
        )

        controle.save()

        return redirect('controle:feito')
    
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

        return redirect('controle:feito')

class Sucesso(View):
    def get(self, request):
        return render(request, 'feito.html')