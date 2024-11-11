from django.shortcuts import render,  HttpResponse

# Create your views here.


def index(request):
    personas = [
        {"nombre": "Juan", "apellido": "Pérez", "edad": 12},
        {"nombre": "Ana", "apellido": "García", "edad": 34},
        {"nombre": "Luis", "apellido": "Martínez", "edad": 10},
        {"nombre": "Sofía", "apellido": "Rodríguez", "edad": 30}
    ]
    contexto = {'personas': personas}
    return render(request, 'index.html', contexto)

def pagina(request):
    return render(request, 'pagina.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def contacto(request, nombre):
    return HttpResponse(f"Contacto: {nombre}")