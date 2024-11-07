""" En Python, un módulo es un archivo que contiene definiciones y declaraciones de funciones, variables y clases 
que puedes utilizar en otros programas. Los módulos permiten organizar el código en componentes reutilizables, 
lo que facilita la gestión y el mantenimiento del código. 
También ayudan a evitar la duplicación y a mantener el código limpio y modular. 


math: Funciones matemáticas avanzadas.
random: Generación de números aleatorios.
datetime: Manejo de fechas y horas.
os: Interacción con el sistema operativo.
sys: Interacción con el intérprete de Python.
json: Manejo de datos en formato JSON.
re: Expresiones regulares.


"""


import math
print(math.sqrt(16))  # Salida: 4.0
# print(dir(math)) 

from math import pi, sqrt
print(pi)          # Salida: 3.141592653589793
print(sqrt(25))    # Salida: 5.0


import math as m
print(m.sqrt(9))  # Salida: 3.0


from math import sqrt as raiz
print(raiz(16))  # Salida: 4.0

