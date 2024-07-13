"""
URL configurations for the Bus Ticket Booking System.

This module contains the main URL configurations for the project, including
the admin interface and the API endpoints.
"""
from django.contrib import admin
from django.urls import path, include
from api.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
