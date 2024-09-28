from django.db import models
from users.models import CustomUser


class Address(models.Model):
    """модель адреса"""
    state = models.CharField(max_length=100,
                            verbose_name='Область')
    city = models.CharField(max_length=100,
                            verbose_name='Город')
    street = models.CharField(max_length=255,
                            verbose_name='Улица')
    house_number = models.CharField(max_length=10,
                                    verbose_name='Номер дома')



class Trips(models.Model):
    """Модель поездки"""
    starting_point = models.ManyToManyField("Address",related_name='trips',
                                            verbose_name='Откуда')
    end_point = models.ManyToManyField("Address",related_name='trips',
                                            verbose_name='Куда')
    date = models.DateTimeField()
    cars = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='car')