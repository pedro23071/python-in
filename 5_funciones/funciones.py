#  Definir una Función
def saludar():
    print("¡Hola, bienvenido!")
    
saludar()


# Funciones con Parámetros
def saludar(nombre):
    print("¡Hola,", nombre, "!")

saludar("Ana")  # Salida: ¡Hola, Ana!


# Funciones con Valor de Retorno
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print("La suma es:", resultado)  # Salida: La suma es: 8

# Parámetros con Valores Predeterminados
def saludar(nombre="Visitante"):
    print("¡Hola,", nombre, "!")

saludar("Carlos")  # Salida: ¡Hola, Carlos!
saludar()          # Salida: ¡Hola, Visitante!


# Funciones con Parámetros Variables (*args y **kwargs)

# *args permite pasar un número variable de argumentos posicionales a la función. Los argumentos se reciben como una tupla.
def sumar(*args):
    resultado = sum(args)
    return resultado

print(sumar(1, 2, 3))       # Salida: 6
print(sumar(4, 5, 6, 7, 8)) # Salida: 30


# **kwargs permite pasar un número variable de argumentos nombrados (clave-valor) a la función. Los argumentos se reciben como un diccionario.

def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Ana", edad=25, ciudad="Madrid")
# Salida:
# nombre: Ana
# edad: 25
# ciudad: Madrid


# *Funciones Lambda
multiplicar = lambda x, y: x * y
print(multiplicar(3, 4))  # Salida: 12
