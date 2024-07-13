"""
Models for the Bus Ticket Booking System.

This module contains the models for Buses, Stops, Seats, Blocking, and Booking.
"""
from django.db import models


class Bus(models.Model):
    """
        Model representing a bus.

        Attributes:
            bus_number (str): The bus number.
            source (str): The source location.
            destination (str): The destination location.
            start_time (time): The start time of the bus.
        """
    bus_number = models.CharField(max_length=20)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.bus_number} ({self.source} to {self.destination})"


class Stop(models.Model):
    """
        Model representing a stop on a bus route.

        Attributes:
            bus (ForeignKey): The bus associated with this stop.
            stop_name (str): The name of the stop.
            stop_time (time): The time the bus stops here.
        """
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    stop_name = models.CharField(max_length=50)
    stop_time = models.TimeField()

    def __str__(self):
        return self.stop_name


class Seat(models.Model):
    """
       Model representing a seat on a bus.

       Attributes:
           bus (ForeignKey): The bus associated with this seat.
           seat_number (str): The seat number.
           is_available (bool): Whether the seat is available.
       """
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.seat_number} ({'Available' if self.is_available else 'Not Available'})"


class Blocking(models.Model):
    """
        Model representing a blocking of seats.

        Attributes:
            bus (ForeignKey): The bus associated with this blocking.
            number_of_passengers (int): The number of passengers.
            pickup_point (ForeignKey): The pickup point.
            blocking_id (str): The unique blocking ID.
        """
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    number_of_passengers = models.IntegerField()
    pickup_point = models.ForeignKey(Stop, on_delete=models.CASCADE)
    blocking_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.blocking_id


class Booking(models.Model):
    """
        Model representing a booking of blocked seats.

        Attributes:
            blocking (ForeignKey): The blocking associated with this booking.
            booking_id (str): The unique booking ID.
            booking_date (datetime): The date and time the booking was made.
        """
    blocking = models.ForeignKey(Blocking, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=50, unique=True)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_id
