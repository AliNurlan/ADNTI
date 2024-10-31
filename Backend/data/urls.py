from django.urls import path,re_path
from . import views

urlpatterns=[
    path('sum/<str:num>', views.sum),
    re_path(r'^about', views.about,kwargs={"name":"Tom", "age": 38}),
    path('',views.index),
    path('a',views.a),
]