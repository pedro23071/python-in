from django.urls import path
from . import views

urlpatterns = [
    path('articles/list/', views.list_articles, name="list_articles"),
]