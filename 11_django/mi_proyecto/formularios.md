# Django Forms: Explicación y Tipos de Inputs

Django proporciona una clase llamada `forms.Form` para definir formularios manualmente y `forms.ModelForm` para generar formularios basados en modelos de la base de datos.

A continuación, se explican las clases de formularios, los tipos de inputs disponibles y cómo llamarlos en un proyecto Django.

---

## **1. Creación de Formularios con `forms.ModelForm`**

`ModelForm` permite crear un formulario automáticamente basado en un modelo definido en `models.py`. Esto reduce el trabajo manual de configurar los campos del formulario.

### Ejemplo:

**`forms.py`:**

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'public', 'img']  # Campos del formulario
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del artículo'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe el contenido'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
```

---

## **2. Tipos de Inputs Disponibles**

Django Forms incluye una variedad de widgets que representan diferentes tipos de inputs HTML. Algunos de los más comunes son:


| Tipo de Input        | Clase Django               | Descripción                              |
| -------------------- | -------------------------- | ----------------------------------------- |
| `TextInput`          | `forms.TextInput`          | Campo de texto simple                     |
| `Textarea`           | `forms.Textarea`           | Área de texto para contenido largo       |
| `EmailInput`         | `forms.EmailInput`         | Campo de texto para correos electrónicos |
| `PasswordInput`      | `forms.PasswordInput`      | Campo para contraseñas                   |
| `CheckboxInput`      | `forms.CheckboxInput`      | Checkbox                                  |
| `Select`             | `forms.Select`             | Menú desplegable                         |
| `RadioSelect`        | `forms.RadioSelect`        | Botones de radio                          |
| `DateInput`          | `forms.DateInput`          | Campo de texto para fechas                |
| `ClearableFileInput` | `forms.ClearableFileInput` | Campo para subir archivos                 |

### Ejemplo de Uso en un Formulario:

```python
from django import forms

class CustomForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    aceptar_terminos = forms.BooleanField(widget=forms.CheckboxInput())
```

---

## **3. Llamar al Formulario en una Vista**

En tu archivo `views.py`, llama al formulario para manejar las solicitudes HTTP:

**`views.py`:**

```python
from django.shortcuts import render, redirect
from .forms import ArticleForm

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})
```

---

## **4. Mostrar el Formulario en una Plantilla**

En tu archivo de plantilla HTML, renderiza el formulario y asegúrate de incluir el token CSRF:

**`create_article.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Crear Artículo</title>
</head>
<body>
    <h1>Crear un Nuevo Artículo</h1>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }} <!-- Renderiza el formulario -->
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
```

---

## **5. Generar el Formulario Manualmente (Opcional)**

Si no usas `ModelForm`, puedes definir los campos manualmente en un formulario.

**`forms.py`:**

```python
from django import forms

class ManualForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido'}))
    public = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
```

---

### Resumen

- **`forms.ModelForm`**: Simplifica la creación de formularios basados en modelos.
- **Widgets**: Controlan cómo se renderizan los inputs en HTML.
- **`views.py`**: Procesa los datos enviados y guarda el formulario.
- **Plantilla HTML**: Renderiza el formulario y permite al usuario interactuar.
