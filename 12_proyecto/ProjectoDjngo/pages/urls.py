from django.urls import path
from . import views as pages_views

urlpatterns = [
    path('pagina/<str:slug>/', pages_views.page, name="pagina"),
]