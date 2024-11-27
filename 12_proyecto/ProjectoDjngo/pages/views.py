from django.http import HttpResponse
from django.shortcuts import render
from .models import Page


def page(request, slug):
    try:
        page = Page.objects.get(slug=slug, visible=True)
        return render(request, 'pages/page.html', {
            "page": page,
        })
    except Page.DoesNotExist:
        return render(request, 'pages/404.html', status=404)
