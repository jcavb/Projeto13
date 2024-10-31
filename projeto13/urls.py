# urls.py do projeto principal
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from jatoba import views as jatoba_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', jatoba_views.login_view, name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('home/', jatoba_views.home, name='home'),
    
    path('signup/', jatoba_views.signup_view, name='signup'),
    
    path('', jatoba_views.home, name='home'),  

    path('tarefas/', jatoba_views.lista_tarefas, name='tarefas'),

    path('protegida/', jatoba_views.pagina_protegida, name='protegida'),

    path('infoculturas/', jatoba_views.buscar_cultura, name='infoculturas'),
    
    path('banana/', jatoba_views.banana_infos, name='banana_infos'),
    
    path('abacate/', jatoba_views.abacate_infos, name='abacate_infos'),
    
    path('brocolis/', jatoba_views.brocolis_infos, name='brocolis_infos'),
    
    path('cenoura/', jatoba_views.cenoura_infos, name='cenoura_infos'),
    
    path('couve/', jatoba_views.couve_infos, name='couve_infos'),
    
    path('macaxeira/', jatoba_views.macaxeira_infos, name='macaxeira_infos'),

    path('rucula/', jatoba_views.rucula_infos, name='rucula_infos'),    
    
    path('tomate/', jatoba_views.tomate_infos, name='tomate_infos'),
    
    # Inclui as rotas do app `calendario`
    path('calendario/', include('calendario.urls')),
]
