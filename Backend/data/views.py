from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Vehicle,
    FuelConsumption,
    MaintenanceRecord,
    WorkActivity,
    Equipment
)
from .serializers import (
    VehicleSerializer,
    FuelConsumptionSerializer,
    MaintenanceRecordSerializer,
    WorkActivitySerializer,
    EquipmentSerializer
)

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления транспортными средствами.
    
    list:
        Получить список всех транспортных средств
    create:
        Создать новое транспортное средство
    retrieve:
        Получить детали конкретного транспортного средства
    update:
        Обновить транспортное средство
    delete:
        Удалить транспортное средство
    """
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['vehicle_type', 'engine_status']
    search_fields = ['vehicle_number', 'vehicle_type']
    ordering_fields = ['last_updated', 'vehicle_number']

class FuelConsumptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FuelConsumption.objects.all()
    serializer_class = FuelConsumptionSerializer

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

class WorkActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WorkActivity.objects.all()
    serializer_class = WorkActivitySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer