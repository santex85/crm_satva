from django.db import models
from booking_management.models import Booking


class Guest(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    def __str__(self):
        return f'Guest for booking id {self.booking.client.last_name}'


class Transfer(models.Model):
    guest = models.ForeignKey(Guest, related_name='transfers', on_delete=models.CASCADE)
    arrival_date = models.DateField()
    approximate_arrival_time = models.TimeField()
    arrival_flight_number = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Transfer'
        verbose_name_plural = 'Transfers'
