from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CustomUserViewSet, CarViewSet, AddressViewSet, TripsViewSet
app_name = 'api'

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('cars', CarViewSet, basename='cars')
router.register('addresses', AddressViewSet, basename='addresses')
router.register('trips', TripsViewSet, basename='trips')

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
    path('', include('djoser.urls'))
]