from django.contrib.auth.models import AbstractUser
from django.db import models

class Car(models.Model):
    """модель машины."""

    car_brands = models.CharField(max_length=100,
                            verbose_name='Марка машины')
    car_models = models.CharField(max_length=100,
                            verbose_name='Модель машины')
    state_number = models.CharField(max_length=100,
                            verbose_name='государственный номер')
    


class CustomUser (AbstractUser):
    """кастомная модель пользователя."""

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=150,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=150,
                                 verbose_name='Фамилия')
    cars = models.ManyToManyField("Сar",related_name='car',
                                            verbose_name='Автомобиль')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    class Meta:
        """Класс мета."""

        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
