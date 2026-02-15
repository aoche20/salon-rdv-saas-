from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Salon, Service
from .serializers import SalonSerializer, ServiceSerializer

class SalonViewSet(ModelViewSet):
    serializer_class = SalonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Salon.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Service.objects.filter(salon__owner=self.request.user)
