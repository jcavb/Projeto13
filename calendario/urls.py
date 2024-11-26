# calendario/urls.py
from django.urls import path
from . import views
from calendario import views

urlpatterns = [
    # Define a URL para a página do calendário
    path('', views.calendario, name='calendario'),
    path('relatorio/pdf/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
]
