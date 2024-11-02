from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Vehicle
from decimal import Decimal

# Create your tests here.

class VehicleAPITest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = APIClient()
        
        # Создаем тестовое транспортное средство
        self.vehicle = Vehicle.objects.create(
            vehicle_number='TEST001',
            vehicle_type='Truck',
            gps_device_id='GPS001',
            last_location_lat=Decimal('51.5074'),
            last_location_long=Decimal('-0.1278'),
            fuel_level=Decimal('75.5'),
            engine_status='running'
        )

    def test_vehicle_list(self):
        # Аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)
        
        # Делаем GET-запрос к API
        response = self.client.get('/api/vehicles/')
        
        # Проверяем успешность запроса
        self.assertEqual(response.status_code, 200)
        
        # Проверяем, что получили правильные данные
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['vehicle_number'], 'TEST001')

    def test_vehicle_create(self):
        self.client.force_authenticate(user=self.user)
        
        # Данные для создания нового транспортного средства
        new_vehicle_data = {
            'vehicle_number': 'TEST002',
            'vehicle_type': 'Car',
            'gps_device_id': 'GPS002',
            'last_location_lat': '51.5074',
            'last_location_long': '-0.1278',
            'fuel_level': '80.5',
            'engine_status': 'stopped'
        }
        
        # Делаем POST-запрос к API
        response = self.client.post('/api/vehicles/', new_vehicle_data, format='json')
        
        # Проверяем успешность создания
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Vehicle.objects.count(), 2)
