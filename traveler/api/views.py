from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from trip.models import Trips, Address
from users.models import CustomUser, Car
from api.serializers import(CustomUserSerializer,
                            CarsSerializer,
                            TripsSerializer,
                            AddressSerializer)
from rest_framework.permissions import IsAuthenticated


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Получение информации о текущем пользователе."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [permissions.AllowAny]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.AllowAny]

class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """Создать поездку с проверкой наличия машины."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        author = serializer.validated_data.get('author')
        date = serializer.validated_data.get('date')

        if not author.cars.exists():
            return Response({"detail": "Пользователь должен иметь хотя бы одну машину для создания поездки."}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)