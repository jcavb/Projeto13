from django.urls import path
from . import views

app_name = 'controle'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('semente/', views.AddSemente.as_view(), name='semente'),
    path('fertilizante/', views.AddFertilizante.as_view(), name='fertilizante'),
    path('sucesso/', views.Sucesso.as_view(), name='sucesso'),
]