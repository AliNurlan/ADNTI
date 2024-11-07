from django.contrib import admin
from .models import (
    Staff,
    Vehicle,
    Equipment,
    FuelConsumption,
    MaintenanceRecord,
    WorkActivity,
    AgriculturalWork
)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'salary')
    search_fields = ('full_name', 'position')
    list_filter = ('position',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status')
    search_fields = ('name', 'type')
    list_filter = ('status', 'type')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status')
    search_fields = ('name', 'type')
    list_filter = ('status', 'type')

@admin.register(FuelConsumption)
class FuelConsumptionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'amount', 'cost')
    search_fields = ('vehicle__name',)
    list_filter = ('date', 'vehicle')

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date', 'description', 'cost')
    search_fields = ('vehicle__name', 'description')
    list_filter = ('date', 'vehicle')

@admin.register(WorkActivity)
class WorkActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'status')
    search_fields = ('name',)
    list_filter = ('date', 'status')

@admin.register(AgriculturalWork)
class AgriculturalWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'field', 'status')
    search_fields = ('name', 'field')
    list_filter = ('date', 'status')
