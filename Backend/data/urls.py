from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'data'

router = DefaultRouter()
router.register(r'staff', views.StaffViewSet)

urlpatterns = [
    path('api/staff/<int:staff_id>/workplaces/', views.get_staff_workplaces, name='staff-workplaces'),
] + router.urls
