from django.contrib import admin
from django.urls import path, include
from core import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
path('admin/', admin.site.urls),
path('dashboard/', include('core.urls')),
path('', lambda request: redirect('login'), name='home'),
path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
