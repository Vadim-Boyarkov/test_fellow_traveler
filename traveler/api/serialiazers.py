from rest_framework import serializers
from djoser.serializers import UserSerializer
from trip.models import Trips , Address
from users.models import CustomUser, Car

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CarsSerializer(serializers.ModelSerializer):
    class Meta:

        model = Car
        fields = (
            'car_brands',
            'car_models',
            'state_number'
        )


class CustomUserSerializer(UserSerializer):
    """Сериалайзер для кастомной модели юзера."""
    cars = CarsSerializer(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = (
            'id', 'email', 'first_name',
            'last_name', 'cars'
        )


class TripsSerializer(serializers.ModelSerializer):
    starting_point = AddressSerializer(many=True)
    end_point = AddressSerializer(many=True)
    author = CustomUserSerializer() 

    class Meta:
        model = Trips
        fields = '__all__'
