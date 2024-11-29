from django.contrib import admin
from django.urls import path, include
from jatoba import views as jatoba_views
from calendario import views as calendario_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('logout/', jatoba_views.logout_view, name='logout'),  # Logout
    path('login/', jatoba_views.login_view, name='login'),  # Login

    path('home/', jatoba_views.home, name='home'),  # Home page
    path('signup/', jatoba_views.signup_view, name='signup'),  # Signup
    path('', jatoba_views.home, name='home'),  # Default Home

    # Inclui as URLs do app jatoba
    path('', include('jatoba.urls')),  

    # Inclui as URLs do app calendario
   path('', include('calendario.urls')),  # Include the 'calendario' app URLs
]
