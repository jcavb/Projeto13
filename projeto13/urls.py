from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from jatoba import views


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

    path('notificacoes/', views.notificacoes, name='notificacoes'),

    path('dashboard/', views.dashboard, name='dashboard'),
]

