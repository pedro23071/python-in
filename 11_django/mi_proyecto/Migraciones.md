## ejecutar el servidor

```bash
python manage.py runserver
```

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


| Campo             | Descripción                                   |
| ----------------- | ---------------------------------------------- |
| `CharField`       | Cadena de texto con longitud máxima definida. |
| `IntegerField`    | Números enteros.                              |
| `FloatField`      | Números decimales flotantes.                  |
| `BooleanField`    | Valores booleanos (`True` o `False`).          |
| `DateField`       | Fecha (`YYYY-MM-DD`).                          |
| `DateTimeField`   | Fecha y hora (`YYYY-MM-DD HH:MM:SS`).          |
| `EmailField`      | Campo para direcciones de correo electrónico. |
| `TextField`       | Texto largo sin límite de longitud.           |
| `ForeignKey`      | Relación uno a muchos con otra tabla.         |
| `ManyToManyField` | Relación muchos a muchos con otra tabla.      |

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

# Django Models: Order By y Limit

En Django, los métodos `order_by()` y slicing (`[:limit]`) se utilizan para ordenar y limitar los resultados de una consulta a la base de datos.

---

## **`order_by()`**: Ordenar Resultados

El método `order_by()` se utiliza para ordenar los resultados de una consulta en base a uno o varios campos del modelo.

### **Uso Básico**

```python
Model.objects.all().order_by('campo')
```

#### Ejemplo:

```python
articulos = Article.objects.all().order_by('title')  # Ordena por título en orden ascendente
```

#### Orden Descendente:

Usa un prefijo `-` para ordenar en orden descendente:

```python
articulos = Article.objects.all().order_by('-created_at')  # Ordena por fecha descendente
```

#### Múltiples Campos:

Puedes ordenar por varios campos:

```python
articulos = Article.objects.all().order_by('public', '-created_at')  
# Ordena por `public` ascendente y luego por `created_at` descendente
```

---

## **Límite de Resultados (`[:limit]`)**

Para limitar el número de registros devueltos, utiliza slicing (`[:n]`) en el queryset.

### **Uso Básico**

```python
Model.objects.all()[:n]
```

#### Ejemplo:

```python
articulos = Article.objects.all()[:5]  # Obtiene los primeros 5 artículos
```

#### Combinar con `order_by()`:

Puedes combinar `order_by()` y slicing para limitar resultados ordenados:

```python
articulos = Article.objects.all().order_by('-created_at')[:3]  
# Obtiene los 3 artículos más recientes.
```

#### Excluir los Primeros Registros (`offset`):

Puedes usar slicing para omitir los primeros registros:

```python
articulos = Article.objects.all()[5:]  # Omite los primeros 5 registros
```

---

## **Ejemplo Completo**

```python
from django.shortcuts import render
from .models import Article

def list_articulos(request):
    # Ordenar por fecha de creación descendente y limitar a 10 resultados
    articulos = Article.objects.all().order_by('-created_at')[:10]
    return render(request, 'index_articulos.html', {'articulos': articulos})
```

---

## **SQL Generado por Django**

- **`order_by('-created_at')`**:

  ```sql
  SELECT * FROM article ORDER BY created_at DESC;
  ```
- **`[:5]`**:

  ```sql
  SELECT * FROM article LIMIT 5;
  ```
- **Combinar `order_by` y `[:5]`**:

  ```sql
  SELECT * FROM article ORDER BY created_at DESC LIMIT 5;
  ```

---

## Resumen


| Función             | Descripción                                                 |
| -------------------- | ------------------------------------------------------------ |
| `order_by('campo')`  | Ordena los resultados en base al campo especificado.         |
| `order_by('-campo')` | Ordena los resultados en orden descendente por el campo.     |
| `[:n]`               | Limita el número de resultados devueltos a los primeros`n`. |
| `[offset:]`          | Excluye los primeros`offset` registros de los resultados.    |

---

### Uso Típico:

```python
articulos = Article.objects.all().order_by('-created_at')[:10]
```

Esto obtiene los 10 artículos más recientes.


# Resumen de Métodos Útiles en Django QuerySet


| Método              | Descripción                                                                 |
| -------------------- | ---------------------------------------------------------------------------- |
| `all()`              | Obtiene todos los registros.                                                 |
| `get()`              | Obtiene un único registro que cumple una condición.                        |
| `filter()`           | Filtra registros que cumplen una condición.                                 |
| `exclude()`          | Excluye registros que cumplen una condición.                                |
| `values()`           | Devuelve un diccionario con campos específicos.                             |
| `values_list()`      | Devuelve listas/tuplas de campos específicos.                               |
| `distinct()`         | Elimina registros duplicados.                                                |
| `first()`, `last()`  | Devuelve el primer o último registro.                                       |
| `count()`            | Cuenta el número de registros.                                              |
| `exists()`           | Verifica si hay registros que cumplen una condición.                        |
| `update()`           | Actualiza registros masivamente.                                             |
| `delete()`           | Elimina registros.                                                           |
| `aggregate()`        | Realiza cálculos como`SUM`, `AVG`, `MAX`, `MIN`, `COUNT`.                   |
| `annotate()`         | Agrega campos calculados al`QuerySet`.                                       |
| `select_related()`   | Optimiza consultas para relaciones`ForeignKey` y `OneToOneField`.            |
| `prefetch_related()` | Optimiza consultas para relaciones`ManyToManyField` y `ForeignKey` inversas. |
| `reverse()`          | Invierte el orden del`QuerySet`.                                             |
| `raw()`              | Ejecuta consultas SQL personalizadas.                                        |
| `defer()`, `only()`  | Carga solo los campos necesarios o excluye campos no necesarios.             |
