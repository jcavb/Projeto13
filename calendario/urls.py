# calendario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Define a URL para a página do calendário
    path('', views.calendario, name='calendario'),
]
