"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from data.views import (
    VehicleViewSet,
    EquipmentViewSet,
    FuelConsumptionViewSet,
    MaintenanceRecordViewSet,
    WorkActivityViewSet,
    vehicles,
    login,
    personal
)

# Настройка документации API
schema_view = get_schema_view(
    openapi.Info(
        title="Fleet Management API",
        default_version='v1',
        description="API для системы управления автопарком",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'fuel-consumption', FuelConsumptionViewSet)
router.register(r'maintenance', MaintenanceRecordViewSet)
router.register(r'work-activities', WorkActivityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles-page/', vehicles, name='vehicles-page'),
    path('login/', login, name='login'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Документация API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('personal/', personal, name='personal'),
]
