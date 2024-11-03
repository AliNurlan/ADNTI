from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('vehicles-page/', views.vehicles, name='vehicles-page'),
]