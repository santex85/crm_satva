from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ClientCategoryChoices(models.TextChoices):
    GROUP_CLIENT = 'GRP', 'Группа'
    INDIVIDUAL_CLIENT = 'IND', 'Гость'


class Clients(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    birth_date = models.DateField()
    client_category = models.CharField(
        max_length=3,
        choices=ClientCategoryChoices.choices,
        default=ClientCategoryChoices.INDIVIDUAL_CLIENT,
    )
    photo = models.ImageField(upload_to='client_photos')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class StatusChoices(models.TextChoices):
    IN_WORK = 'INW', 'В работе'
    AWAITING_RESERVATION = 'AWR', 'Жду брони'
    RESERVED = 'RES', 'Забронировал'


class Booking(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=StatusChoices.choices,
        default=StatusChoices.IN_WORK,
    )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    flight_number = models.CharField(max_length=255, null=True, blank=True)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2)
    deposit = models.DecimalField(max_digits=9, decimal_places=2)
    room_number = models.CharField(max_length=50, null=True, blank=True)
    transfer_info = models.TextField(null=True, blank=True)
    transfer_cost = models.DecimalField(max_digits=9, decimal_places=2)
    discounts = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    total_payment_due = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

