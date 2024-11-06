from django.contrib import admin
from .models import (
    Vehicle,
    Equipment,
    FuelConsumption,
    MaintenanceRecord,
    WorkActivity,
    AgriculturalWork
)

admin.site.register(Vehicle)
admin.site.register(Equipment)
admin.site.register(FuelConsumption)
admin.site.register(MaintenanceRecord)
admin.site.register(WorkActivity)
admin.site.register(AgriculturalWork)
