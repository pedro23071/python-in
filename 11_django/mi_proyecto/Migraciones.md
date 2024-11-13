# Django Models y Seeders

## Modelos: Definición en `models.py`

Archivo: `myapp/models.py`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public = models.BooleanField()
    img = models.ImageField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Comandos para Migraciones

Ejecuta los siguientes comandos en la línea de comandos para aplicar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Campos Comunes en los Modelos

Django ofrece una amplia variedad de tipos de campo para definir los datos en tus modelos. Algunos de los más comunes son:

| Campo            | Descripción                                            |
|------------------|--------------------------------------------------------|
| `CharField`      | Cadena de texto con longitud máxima definida.          |
| `IntegerField`   | Números enteros.                                       |
| `FloatField`     | Números decimales flotantes.                           |
| `BooleanField`   | Valores booleanos (`True` o `False`).                  |
| `DateField`      | Fecha (`YYYY-MM-DD`).                                  |
| `DateTimeField`  | Fecha y hora (`YYYY-MM-DD HH:MM:SS`).                  |
| `EmailField`     | Campo para direcciones de correo electrónico.          |
| `TextField`      | Texto largo sin límite de longitud.                    |
| `ForeignKey`     | Relación uno a muchos con otra tabla.                  |
| `ManyToManyField`| Relación muchos a muchos con otra tabla.               |

---

## Crear un Archivo para los Seeders

Estructura del proyecto:

```
mi_proyecto/
│
├── mi_app/
│   ├── models.py
│   ├── seeder.py  # Aquí escribirás los seeders
│
├── manage.py
```

---

## Escribir el Seeder para las Tablas

Archivo: `mi_app/seeder.py`

```python
from mi_app.models import Article, Category
import random

def run_seeders():
    # Crear categorías de ejemplo
    categories = []
    for i in range(5):  # Crea 5 categorías
        category = Category.objects.create(
            name=f"Categoría {i+1}",
            description=f"Descripción de la categoría {i+1}"
        )
        categories.append(category)
    print(f"Se crearon {len(categories)} categorías.")

    # Crear artículos de ejemplo
    for i in range(20):  # Crea 20 artículos
        Article.objects.create(
            title=f"Título del Artículo {i+1}",
            content=f"Este es el contenido del artículo {i+1}.",
            public=random.choice([True, False]),
            img='',  # Opcional: Puedes agregar imágenes reales si lo deseas
            created_at=None,  # Deja que Django asigne automáticamente
            updated_at=None,
        )
    print("Se crearon 20 artículos.")
```

---

## Ejecutar el Seeder desde Django Shell

Abre el shell de Django:

```bash
python manage.py shell
```

Ejecuta el seeder desde el shell:

```python
from mi_app.seeder import run_seeders
run_seeders()
```

---

Este formato organiza la información en secciones claras y utiliza elementos de Markdown como tablas, bloques de código y encabezados para mejorar la legibilidad. ¡Listo para compartir o documentar en tu proyecto! 😊

