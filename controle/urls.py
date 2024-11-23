from django.urls import path
from . import views

app_name = 'controle'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('fertilizante/', views.AddFertilizante.as_view(), name='fertilizante'),
    path('fertilizantes/', views.VerFertilizante.as_view(), name='visualizar_fert'),
    path('fertilizante/<int:id>/delete/', views.delete_fertilizante_view, name='delete_fert'),
    path('semente/', views.AddSemente.as_view(), name='semente'),
    path('sementes/', views.VerSemente.as_view(), name='visualizar_sem'),
    path('semente/<int:id>/delete/', views.delete_semente_view, name='delete_sem'),
    path('rotacao/', views.Rotacao.as_view(), name='rotacao'),
]