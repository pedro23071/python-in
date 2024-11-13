from myapp.models import Article, Category
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




