from django.urls import path,re_path,include
from . import views

product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]

urlpatterns=[
    path("vehicles", views.vehicles),
    path("products/<int:id>/", include(product_patterns)),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user),
    re_path(r"^postuser", views.postuser),
    path('sum/<str:num>', views.sum),
    re_path(r'^about', views.about,kwargs={"name":"Tom", "age": 38}),
    path("set", views.set),
    path("get", views.get),
    path('json_response/',views.json_response),
    path('json/',views.json),
    path('b/',views.index2),
    path('',views.index),
    path('connection',views.connection),
    path('access',views.access),
    path('a',views.a),
]