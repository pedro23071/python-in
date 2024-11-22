from django.shortcuts import get_object_or_404, render,  HttpResponse, redirect
from django.http import Http404
from myapp.models import Article
from myapp.forms import ArticleForm
from django.contrib import messages

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


""" ---------- empiezan los metodos CRUD para articulos ---------- """

def create_articulo(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el nuevo artículo en la base de datos
            
            messages.success(request, 'Articulo creado existosamente')
            return redirect('listar_articulos')  # Cambia esto a la URL que desees redirigir
    else:
        form = ArticleForm()
    return render(request, 'create_articulo.html', {'form': form})



def update_artuculo(request, articulo_id):
    article = get_object_or_404(Article, id=articulo_id)
    if request.method == 'POST':
        # Vincular el formulario con los datos enviados y la instancia del artículo
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()  # Actualizar el artículo existente
            messages.success(request, 'Articulo Editado existosamente')
            return redirect('listar_articulos')  # Redirigir a otra vista (lista de artículos, por ejemplo)
    else:
        # Crear el formulario con la instancia del artículo
        form = ArticleForm(instance=article)

    return render(request, 'edit_article.html', {'form': form})


def artuculo(request, articulo_id):
    try:
        articulo = Article.objects.get(id=articulo_id)
        response = f"Articulo: {articulo.title} - {articulo.content}"
    except:
        response = "Articulo no encontrado"
    return HttpResponse(response)




def list_articulos(request):
    articulos = Article.objects.all()
    return render(request, 'index_articulos.html', {'articulos': articulos})




def editar_articulo(request, articulo_id):
    articulo = Article.objects.get(id=articulo_id)
    articulo.title = "Articulo editado con su nuevo titulo"
    articulo.content = "Articulo editado con su nuevo contenido ..."
    articulo.public = True
    
    articulo.save()
    
    return HttpResponse(f"Articulo {articulo.id} editado: {articulo.title} - {articulo.content}")



def eliminar_articulo(request, articulo_id):
    try:
        articulo = Article.objects.get(id=articulo_id)
        articulo.delete()
        
        messages.success(request, 'Articulo eliminado existosamente')
        # Redirigir o devolver una respuesta
        return redirect('listar_articulos')  # Redirigir a la lista de artículos
    except:
        raise Http404("El artículo no existe.")