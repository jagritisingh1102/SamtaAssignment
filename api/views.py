"""
Views for the Bus Ticket Booking System.

This module contains viewsets for Buses, Stops, Seats, Blocking, and Booking,
as well as views for user registration.
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Bus, Stop, Seat, Blocking, Booking
from .serializers import BusSerializer, StopSerializer, SeatSerializer, BlockingSerializer, BookingSerializer, \
    UserSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class BusViewSet(viewsets.ModelViewSet):
    """
        ViewSet for viewing and editing Bus instances.
    """
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['source', 'destination']
    search_fields = ['bus_number', 'source', 'destination']
    ordering_fields = ['start_time']


class StopViewSet(viewsets.ModelViewSet):
    """
        ViewSet for viewing and editing Stop instances.
    """
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['bus', 'stop_name']
    search_fields = ['stop_name']
    ordering_fields = ['stop_time']


class SeatViewSet(viewsets.ModelViewSet):
    """
        ViewSet for viewing and editing Seat instances.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['bus', 'is_available']
    search_fields = ['seat_number']
    ordering_fields = ['seat_number']


class BlockingViewSet(viewsets.ModelViewSet):
    """
        ViewSet for viewing and editing Blocking instances.
    """
    queryset = Blocking.objects.all()
    serializer_class = BlockingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['bus', 'pickup_point']
    search_fields = ['blocking_id']
    ordering_fields = ['number_of_passengers']


class BookingViewSet(viewsets.ModelViewSet):
    """
        ViewSet for viewing and editing Booking instances.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['blocking']
    search_fields = ['booking_id']
    ordering_fields = ['booking_date']


class RegisterView(generics.CreateAPIView):
    """
        View for user registration.

        Allows new users to register by providing username, email, and password.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
