""" Resumen de Métodos y Funciones para Listas
Funciones generales: len(), max(), min(), sum(), sorted()
Métodos de lista: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse() """


# Iterando sobre una lista
frutas = ["manzana", "banana", "cereza"]

frutas.append('naranja')
print(frutas)

for fruta in frutas:
     print(f"{frutas.index(fruta)} {fruta}")
  

# *Funciones Comunes para Listas        
numeros = [1, 2, 3, 4, 5]
print(len(numeros))  # Salida: 5
print(max(numeros))  # Salida: 5
print(min(numeros))  # Salida: 1
print(sum(numeros))  # Salida: 15
# sorted(lista): Devuelve una nueva lista ordenada de menor a mayor (la lista original no cambia).
print(sorted(numeros, reverse=True))  # Salida: [5, 4, 3, 2, 1]

cadena = "hola"
print(list(cadena))  # Salida: ['h', 'o', 'l', 'a']


# *Métodos Comunes para Listas
numeros.append(6)
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6]

# extend(iterable): Agrega todos los elementos de un iterable (otra lista, tupla, etc.) al final de la lista.
numeros.extend([7, 8])
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8]

# insert(posicion, elemento): Inserta un elemento en una posición específica.
numeros.insert(0, 0)
print(numeros)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# remove(elemento): Elimina la primera aparición de un elemento en la lista.
numeros.remove(3)
print(numeros)  # Salida: [0, 1, 2, 4, 5, 6, 7, 8]


# pop([indice]): Elimina y devuelve el elemento en el índice especificado. Si no se especifica un índice, elimina y devuelve el último elemento.
ultimo = numeros.pop()  # Sin índice
print(ultimo)           # Salida: 8
print(numeros)          # Salida: [0, 1, 2, 4, 5, 6, 7]

segundo = numeros.pop(1)  # Con índice
print(segundo)            # Salida: 1
print(numeros)            # Salida: [0, 2, 4, 5, 6, 7]


# clear(): Elimina todos los elementos de la lista.
numeros.clear()
print(numeros)  # Salida: []

# index(elemento, [inicio, [fin]]): Devuelve el índice de la primera aparición de un elemento en la lista. Opcionalmente, se puede especificar un rango de búsqueda con inicio y fin.
numeros = [1, 2, 3, 4, 5]
print(numeros.index(3))  # Salida: 2


# count(elemento): Devuelve el número de veces que un elemento aparece en la lista.
print(numeros.count(2))  # Salida: 1


# sort(key=None, reverse=False): Ordena los elementos de la lista en orden ascendente. Puede ordenar en orden descendente con reverse=True y acepta una key de ordenamiento.
numeros.sort(reverse=True)
print(numeros)  # Salida: [5, 4, 3, 2, 1]

# reverse(): Invierte el orden de los elementos de la lista.
numeros.reverse()
print(numeros)  # Salida: [1, 2, 3, 4, 5]
