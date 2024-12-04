from django.shortcuts import render
from .models import Article

# Create your views here.
def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'article/list.html', {
        'title': 'Listado de Articulos',
        'articles_list': articles,
     })