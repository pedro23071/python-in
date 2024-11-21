"""mi_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from myapp import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.index, name="index"),
    path('pagina/', myapp_views.pagina, name="pagina"),
    path('hola-mundo/', myapp_views.hola_mundo, name="hola_mundo"),
    path('contacto/<str:nombre>/', myapp_views.contacto, name="contacto"),
    path('crear-articulo/<str:titulo>/<str:content>/<str:public>/', myapp_views.crear_articulo, name="crear_articulo"),
    path('articulo/<int:articulo_id>/', myapp_views.artuculo, name="get_articulo"),
    path('editar-articulo/<int:articulo_id>/', myapp_views.editar_articulo, name="editar_articulo"),
    path('list-articulo/', myapp_views.list_articulos, name="listar_articulos"),
    path('delete-articulo/<int:articulo_id>/', myapp_views.eliminar_articulo, name="eliminar_articulo"),
    path('create-articulo/', myapp_views.create_articulo, name="create_articulo"),
    path('save-articulo/<int:articulo_id>/', myapp_views.save_articulo, name="save")
]

