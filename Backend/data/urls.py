from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'data'

router = DefaultRouter()
router.register(r'staff', views.StaffViewSet)

urlpatterns = [
    path('vehicles-page/', views.vehicles, name='vehicles-page'),
    path('login/', views.login, name='login'),
    path('api/staff/<int:staff_id>/workplaces/', views.get_staff_workplaces, name='staff-workplaces'),
    path('staff/<str:position>/', views.staff_list, name='staff_list'),
    path('personal/', views.personal, name='personal'),
    path('api/', include(router.urls)),
]
