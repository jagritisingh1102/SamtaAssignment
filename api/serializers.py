"""
Serializers for the Bus Ticket Booking System.

This module contains serializers for Buses, Stops, Seats, Blocking, and Booking.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bus, Stop, Seat, Blocking, Booking


class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for the User model.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BusSerializer(serializers.ModelSerializer):
    """
        Serializer for the Bus model.
    """
    class Meta:
        model = Bus
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    """
        Serializer for the Stop model.
    """
    class Meta:
        model = Stop
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    """
        Serializer for the Seat model.
    """
    class Meta:
        model = Seat
        fields = '__all__'


class BlockingSerializer(serializers.ModelSerializer):
    """
        Serializer for the Blocking model.
    """
    class Meta:
        model = Blocking
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """
        Serializer for the Booking model.
    """
    class Meta:
        model = Booking
        fields = '__all__'
