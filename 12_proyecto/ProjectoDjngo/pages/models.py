from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    slug =  models.CharField(unique=True, max_length=150, verbose_name='URL Amigable')
    order = models.IntegerField(default=0, verbose_name='Orden')
    is_nav = models.BooleanField(default=False, verbose_name='En Navegacion')
    visible = models.BooleanField(verbose_name='Visible')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        
        
    def __str__(self):
        return self.title
        