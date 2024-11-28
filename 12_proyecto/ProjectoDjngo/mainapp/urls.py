from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index_vacio"),
    path('inicio/', views.index, name="index"),
]