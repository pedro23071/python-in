# Iterando sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterando con rango de números
for i in range(4):
     print(f"contador range {i}")  # Imprime los números del 0 al 4
else:
    print("Fin del bucle for 1")
    

contador = 1
while contador <= 5:
    print(f"contador while {contador}")
    contador += 1  # Incremento para evitar un bucle infinito


contador = 0
for i in range(5):
    if i == 3:
        continue  # Salta la iteración cuando i es igual a 3
    print(i)  # Imprime 0, 1, 2, 4
else:
    print("Fin del bucle while 2")


""" Resumen
for: Se utiliza para iterar sobre secuencias y rangos.
while: Ejecuta el código mientras la condición sea verdadera.
break: Finaliza el bucle.
continue: Salta a la siguiente iteración.
else en bucles: Se ejecuta solo si el bucle termina sin interrupciones. """

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Al iterar directamente sobre el diccionario, obtendrás cada una de las claves.
for clave in diccionario:
    print(clave)

# Puedes usar el método .values() para iterar sobre los valores del diccionario.
for valor in diccionario.values():
    print(valor)


for clave, valor in diccionario.items():
    print(clave, "=>", valor)
