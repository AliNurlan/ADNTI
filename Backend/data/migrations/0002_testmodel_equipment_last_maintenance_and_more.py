# Generated by Django 5.1.2 on 2024-11-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='last_maintenance',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='next_maintenance_due',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='fuelconsumption',
            name='odometer_reading',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintenancerecord',
            name='parts_replaced',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='maintenancerecord',
            name='technician',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine_status',
            field=models.CharField(choices=[('running', 'Running'), ('stopped', 'Stopped'), ('maintenance', 'Under Maintenance')], default='stopped', max_length=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_level',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tire_pressure_front_left',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tire_pressure_front_right',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tire_pressure_rear_left',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='tire_pressure_rear_right',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='workactivity',
            name='distance_covered',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='workactivity',
            name='fuel_consumed',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
