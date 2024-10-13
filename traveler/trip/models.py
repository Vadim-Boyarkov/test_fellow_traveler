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
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    starting_point = models.ManyToManyField("Address",related_name='starting_point_trips',
                                            verbose_name='Откуда')
    end_point = models.ManyToManyField("Address",related_name='end_point_trips',
                                            verbose_name='Куда')
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
#   cars = models.OneToOneField(CustomUser.cars,
#                                on_delete=models.CASCADE,
#                                related_name='car')
# Поле cars должно подтянуться с модели юзера