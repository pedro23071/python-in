from django.shortcuts import render,  HttpResponse, redirect
from django.http import Http404
from myapp.models import Article

# Create your views here.
personas = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 12},
    {"nombre": "Ana", "apellido": "García", "edad": 34},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 10},
    {"nombre": "Sofía", "apellido": "Rodríguez", "edad": 30}
]

def index(request):
    contexto = {'personas': personas}
    return render(request, 'index.html', contexto)

def pagina(request):
    return render(request, 'pagina.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def contacto(request, nombre):
    return HttpResponse(f"Contacto: {nombre}")

def crear_articulo(request, titulo, content, public):
    articulo = Article(
        title = titulo,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"articulo creado {articulo.title} - {articulo.content}")


def artuculo(request, articulo_id):
    try:
        articulo = Article.objects.get(id=articulo_id)
        response = f"Articulo: {articulo.title} - {articulo.content}"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)


def editar_articulo(request, articulo_id):
    articulo = Article.objects.get(id=articulo_id)
    articulo.title = "Articulo editado con su nuevo titulo"
    articulo.content = "Articulo editado con su nuevo contenido ..."
    articulo.public = True
    
    articulo.save()
    
    return HttpResponse(f"Articulo {articulo.id} editado: {articulo.title} - {articulo.content}")


def list_articulos(request):
    articulos = Article.objects.all()
    return render(request, 'index_articulos.html', {'articulos': articulos})

def eliminar_articulo(request, articulo_id):
    try:
        articulo = Article.objects.get(id=articulo_id)
        articulo.delete()
        # Redirigir o devolver una respuesta
        return redirect('listar_articulos')  # Redirigir a la lista de artículos
    except:
        raise Http404("El artículo no existe.")