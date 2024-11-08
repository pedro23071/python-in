from django.shortcuts import render,  HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hola desde INICIO")

def pagina(request):
    return HttpResponse("hola desde Pagina")

def hola_mundo(request):
    return HttpResponse("Hola mundo desde mi controlador")


