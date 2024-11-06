from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
from django.db import models

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=100)
    gps_device_id = models.CharField(max_length=100, unique=True)
    last_location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    last_location_long = models.DecimalField(max_digits=9, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)
    tire_pressure_front_left = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tire_pressure_front_right = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tire_pressure_rear_left = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tire_pressure_rear_right = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fuel_level = models.DecimalField(max_digits=5, decimal_places=2)
    engine_status = models.CharField(max_length=20, choices=[
        ('running', 'Running'),
        ('stopped', 'Stopped'),
        ('maintenance', 'Under Maintenance')
    ])

    def __str__(self):
        return f"{self.vehicle_type} - {self.vehicle_number}"

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('operational', 'Operational'),
            ('maintenance', 'Under Maintenance'),
            ('repair', 'Under Repair'),
            ('inactive', 'Inactive')
        ]
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    last_maintenance = models.DateTimeField(null=True)
    next_maintenance_due = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.name} ({self.equipment_type})"

class FuelConsumption(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    fuel_type = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    odometer_reading = models.IntegerField()
    
    def __str__(self):
        return f"{self.vehicle.vehicle_number} - {self.timestamp}"

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=100)
    description = models.TextField()
    date_performed = models.DateTimeField()
    next_maintenance_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    technician = models.CharField(max_length=100)
    parts_replaced = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.vehicle.vehicle_number} - {self.maintenance_type}"

class WorkActivity(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_long = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    fuel_consumed = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    distance_covered = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    def __str__(self):
        return f"{self.vehicle.vehicle_number} - {self.activity_type}"

class Staff(models.Model):
    POSITION_CHOICES = [
        ('Программист', 'Программист'),
        ('Эколог', 'Эколог'),
        ('Бухгалтер', 'Бухгалтер'),
        ('Тракторист', 'Тракторист'),
        ('Комбайнер', 'Комбайнер'),
        ('Электрик', 'Электрик'),
        ('Инженер', 'Инженер'),
        ('Агроном', 'Агроном'),
        ('Менеджер', 'Менеджер'),
    ]

    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(
        max_length=100, 
        verbose_name="Должность",
        choices=POSITION_CHOICES
    )
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Зарплата",
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.full_name} - {self.position}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['full_name']  # сортировка по умолчанию
