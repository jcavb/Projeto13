from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from jatoba import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('home/', views.home, name='home'),
    
    path('signup/', views.signup, name='signup'),
    
    path('', views.home, name='home'),  

    path('dashboard/', views.dashboard, name='dashboard'),

    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),

    path('protegida/', views.pagina_protegida, name='pagina_protegida'),
]

