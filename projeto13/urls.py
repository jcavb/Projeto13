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

    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),

    path('protegida/', views.pagina_protegida, name='protegida'),
]

