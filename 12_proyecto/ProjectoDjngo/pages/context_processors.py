from .models import Page


def get_pages(request):
    pages = Page.objects.filter(visible=True, is_nav=True).values_list('id', 'title', 'slug').order_by('order')
    return {
        'pages': pages
    }