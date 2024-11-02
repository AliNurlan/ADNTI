from rest_framework import serializers
from .models import Vehicle, Equipment, FuelConsumption, MaintenanceRecord, WorkActivity

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class FuelConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelConsumption
        fields = '__all__'

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'

class WorkActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkActivity
        fields = '__all__' 