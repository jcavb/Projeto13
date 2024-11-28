from django.urls import path # type: ignore
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'jatoba'

urlpatterns = [
    path('tarefas/', views.lista_tarefas, name='tarefas'),

    path('protegida/', views.pagina_protegida, name='protegida'),

    path('infoculturas/', views.buscar_cultura, name='infoculturas'),
    
    path('banana/', views.banana_infos, name='banana_infos'),
    
    path('abacate/', views.abacate_infos, name='abacate_infos'),
    
    path('brocolis/', views.brocolis_infos, name='brocolis_infos'),
    
    path('cenoura/', views.cenoura_infos, name='cenoura_infos'),
    
    path('couve/', views.couve_infos, name='couve_infos'),
    
    path('macaxeira/', views.macaxeira_infos, name='macaxeira_infos'),

    path('rucula/', views.rucula_infos, name='rucula_infos'),    
    path('menu/', views.menu_view, name='menu'),  # Adiciona a rota para o menu
    path('tomate/', views.tomate_infos, name='tomate_infos'),
    path('fertilizante/', views.AddFertilizante.as_view(), name='fertilizante'),
    path('fertilizantes/', views.VerFertilizante.as_view(), name='visualizar_fert'),
    path('fertilizante/<int:id>/delete/', views.delete_fertilizante_view, name='delete_fert'),
    path('semente/', views.AddSemente.as_view(), name='semente'),
    path('sementes/', views.VerSemente.as_view(), name='visualizar_sem'),
    path('semente/<int:id>/delete/', views.delete_semente_view, name='delete_sem'),
    path('rotacao/', views.Rotacao.as_view(), name='rotacao'),
]
