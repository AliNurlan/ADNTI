from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Vehicle,
    FuelConsumption,
    MaintenanceRecord,
    WorkActivity,
    Equipment,
    Staff
)
from .serializers import (
    VehicleSerializer,
    FuelConsumptionSerializer,
    MaintenanceRecordSerializer,
    WorkActivitySerializer,
    EquipmentSerializer,
    StaffSerializer
)
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

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

class StaffViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'position']
    ordering_fields = ['full_name', 'salary']

def vehicles(request):
    """
    Отображает страницу со списком транспортных средств
    """
    return render(request, 'vehicles.html')

def login(request):
    """
    Отображает страницу со списком
    """
    return render(request, 'auto.html')

def personal(request):
    """
    Отображает страницу персонала
    """
    staff_data = Staff.objects.all()
    return render(request, 'personal.html', {'staff_data': staff_data})

@require_http_methods(["GET"])
def get_staff_workplaces(request, staff_id):
    try:
        staff = Staff.objects.get(id=staff_id)
        return JsonResponse({
            'workplaces': {
                'full_name': staff.full_name,
                'position': staff.position,
                'salary': str(staff.salary)
            }
        })
    except Staff.DoesNotExist:
        return JsonResponse({'error': 'Сотрудник не найден'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)