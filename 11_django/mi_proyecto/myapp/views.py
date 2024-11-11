from django.shortcuts import render,  HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def pagina(request):
    return render(request, 'pagina.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def contacto(request, nombre):
    return HttpResponse(f"Contacto: {nombre}")