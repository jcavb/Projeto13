from django.contrib import admin
from django.urls import path
from . import views
from calendario import views

app_name = 'calendario'

urlpatterns = [
    # Define a URL para a página do calendário
    path('', views.calendario, name='calendario'),
    path('gerar-pdf/', views.gerar_pdf_simples, name='gerar_pdf'),
      path('adicionar-observacao/', views.gerar_pdf_com_observacao, name='gerar_pdf_com_observacao'),
]
