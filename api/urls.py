"""
URL configurations for the Bus Ticket Booking System API.

This module contains URL configurations for the API endpoints including buses, stops, seats, blockings, and bookings,
as well as user registration, login, and logout views.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusViewSet, StopViewSet, SeatViewSet, BlockingViewSet, BookingViewSet, RegisterView
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'buses', BusViewSet)
router.register(r'stops', StopViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'blockings', BlockingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
