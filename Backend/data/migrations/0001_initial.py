# Generated by Django 5.1.2 on 2024-11-06 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgriculturalWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(choices=[('plowing', 'Вспашка'), ('seeding', 'Посев'), ('harvesting', 'Уборка'), ('fertilizing', 'Внесение удобрений')], max_length=20)),
                ('field_name', models.CharField(max_length=100)),
                ('crop_type', models.CharField(max_length=100)),
                ('machinery', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('planned', 'Запланировано'), ('in_progress', 'В процессе'), ('completed', 'Завершено')], default='planned', max_length=20)),
                ('progress', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('planned_end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=50, unique=True)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('gps_device_id', models.CharField(max_length=100, unique=True)),
                ('last_location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('last_location_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('tire_pressure_front_left', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('tire_pressure_front_right', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('tire_pressure_rear_left', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('tire_pressure_rear_right', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('fuel_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('engine_status', models.CharField(choices=[('running', 'Running'), ('stopped', 'Stopped'), ('maintenance', 'Under Maintenance')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_performed', models.DateTimeField()),
                ('next_maintenance_date', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('technician', models.CharField(max_length=100)),
                ('parts_replaced', models.TextField(blank=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='FuelConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fuel_type', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('odometer_reading', models.IntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('equipment_type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('operational', 'Operational'), ('maintenance', 'Under Maintenance'), ('repair', 'Under Repair'), ('inactive', 'Inactive')], max_length=20)),
                ('last_maintenance', models.DateTimeField(null=True)),
                ('next_maintenance_due', models.DateTimeField(null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='WorkActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField()),
                ('fuel_consumed', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('distance_covered', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.vehicle')),
            ],
        ),
    ]
