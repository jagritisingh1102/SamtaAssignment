"""
Admin configuration for the Bus Ticket Booking System.

This module contains the admin configurations for managing Buses, Stops, Seats, Blocking, and Booking.
"""
from .models import Bus, Stop, Seat, Blocking, Booking
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
        Custom form for creating new users in the admin interface.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)


class CustomUserChangeForm(UserChangeForm):
    """
        Custom form for changing user details in the admin interface.
    """

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'email',)


class UserAdmin(BaseUserAdmin):
    """
        Custom admin class for managing users.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )


class BusAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Bus model.
    """
    list_display = ('bus_number', 'source', 'destination', 'start_time')
    search_fields = ('bus_number', 'source', 'destination')


class StopAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Stop model.
    """
    list_display = ('bus', 'stop_name', 'stop_time')
    search_fields = ('bus__bus_number', 'stop_name')


class SeatAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Seat model.
    """
    list_display = ('bus', 'seat_number', 'is_available')
    search_fields = ('bus__bus_number', 'seat_number')


class BlockingAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Blocking model.
    """
    list_display = ('bus', 'number_of_passengers', 'pickup_point', 'blocking_id')
    search_fields = ('bus__bus_number', 'blocking_id')


class BookingAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Booking model.
    """
    list_display = ('blocking', 'booking_id', 'booking_date')
    search_fields = ('blocking__blocking_id', 'booking_id')


# Registering the admin configurations
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Stop, StopAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Blocking, BlockingAdmin)
admin.site.register(Booking, BookingAdmin)
