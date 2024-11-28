from django.contrib import admin
from django.urls import path
from . import views
from calendario import views

app_name = 'calendario'

urlpatterns = [
    # Define a URL para a página do calendário
    path('', views.calendario, name='calendario'),
    path('relatorio/pdf/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
    path('adicionar-observacao/', views.adicionar_observacao, name='adicionar_observacao'),
    path('gerar-pdf/', views.gerar_pdf_com_observacao, name='gerar_pdf_com_observacao'),
]
