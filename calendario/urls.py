from django.contrib import admin
from django.urls import path
from . import views
from calendario import views
from .views import adicionar_observacao
app_name = 'calendario'

urlpatterns = [
    # Define a URL para a página do calendário
    path('calendario/', views.calendario, name='calendario'),
    path('adicionar-observacao/', adicionar_observacao, name='adicionar_observacao'),
]
