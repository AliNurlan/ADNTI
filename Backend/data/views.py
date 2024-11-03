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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['vehicle_number', 'vehicle_type', 'engine_status']
    ordering_fields = ['last_updated', 'vehicle_number']

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        vehicle_type = self.request.query_params.get('vehicle_type', None)
        engine_status = self.request.query_params.get('engine_status', None)
        
        if vehicle_type:
            queryset = queryset.filter(vehicle_type=vehicle_type)
        if engine_status:
            queryset = queryset.filter(engine_status=engine_status)
            
        return queryset

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

def vehicles(request):
    return render(request, 'vehicles.html')