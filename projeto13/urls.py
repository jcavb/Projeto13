from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from jatoba import views
from calendario import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', views.login_view, name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('home/', views.home, name='home'),
    
    path('signup/', views.signup_view, name='signup'),
    
    path('', views.home, name='home'),  

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
    
    path('tomate/', views.tomate_infos, name='tomate_infos'),
    path('fertilizante/', views.AddFertilizante.as_view(), name='fertilizante'),
    path('fertilizantes/', views.VerFertilizante.as_view(), name='visualizar_fert'),
    path('fertilizante/<int:id>/delete/', views.delete_fertilizante_view, name='delete_fert'),
    path('semente/', views.AddSemente.as_view(), name='semente'),
    path('sementes/', views.VerSemente.as_view(), name='visualizar_sem'),
    path('semente/<int:id>/delete/', views.delete_semente_view, name='delete_sem'),
    path('rotacao/', views.Rotacao.as_view(), name='rotacao'),
    path('calendario/', include('calendario.urls')),  # Inclui as URLs do app `calendario`
    path('', include('jatoba.urls')),  # Inclui as URLs do app `jatoba`
    
]

