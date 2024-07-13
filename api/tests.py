"""
Unittests for the Bus Ticket Booking System.

This module contains unittests for testing the API endpoints of the Bus Ticket Booking System.
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Bus, Stop, Seat, Blocking, Booking
from django.contrib.auth.models import User


class BusTicketServiceTests(TestCase):
    """
        Test suite for the Bus Ticket Booking System API.
    """
    def setUp(self):
        """
            Set up the test environment.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.bus1 = Bus.objects.create(bus_number='1001', source='New York', destination='Boston',
                                       start_time='08:00:00')
        self.bus2 = Bus.objects.create(bus_number='1002', source='New York', destination='Chicago',
                                       start_time='09:00:00')
        self.stop1 = Stop.objects.create(bus=self.bus1, stop_name='Central', stop_time='08:30:00')
        self.seat1 = Seat.objects.create(bus=self.bus1, seat_number='1A', is_available=True)
        self.blocking1 = Blocking.objects.create(bus=self.bus1, number_of_passengers=2, pickup_point=self.stop1,
                                                 blocking_id='block123')
        self.booking1 = Booking.objects.create(blocking=self.blocking1, booking_id='book123')

    def test_bus_search(self):
        """
            Test the bus search functionality.
        """
        response = self.client.get(reverse('bus-list'), {'search': 'New York'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_bus_filter(self):
        """
            Test filtering buses by source and destination.
        """
        response = self.client.get(reverse('bus-list'), {'source': 'New York', 'destination': 'Boston'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['bus_number'], '1001')

    def test_stop_search(self):
        """
            Test the stop search functionality.
        """
        response = self.client.get(reverse('stop-list'), {'search': 'Central'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_seat_ordering(self):
        """
            Test ordering seats by seat number.
        """
        response = self.client.get(reverse('seat-list'), {'ordering': 'seat_number'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_blocking_search(self):
        """
            Test the blocking search functionality.
        """
        response = self.client.get(reverse('blocking-list'), {'search': 'block123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_booking_search(self):
        """
            Test the booking search functionality.
        """
        response = self.client.get(reverse('booking-list'), {'search': 'book123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
