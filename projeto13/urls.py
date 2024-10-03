from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('home/', views.home, name='home'),
    
    path('signup/', views.signup, name='signup'),
    
    path('', views.home, name='home'),  
]
