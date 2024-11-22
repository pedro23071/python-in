from django import forms
from myapp.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'public', 'img']  # Campos que estarán en el formulario
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del artículo'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe el contenido'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input', 'checked': True}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'public': '¿Es público?',
            'img': 'Imagen',
        }
        help_texts = {
            'title': 'Escribe un título descriptivo para el artículo.',
            'img': 'Opcional: Puedes cargar una imagen para el artículo.',
        }
        error_messages = {
            'title': {
                'max_length': 'El título no puede tener más de 200 caracteres.',
            },
        }
