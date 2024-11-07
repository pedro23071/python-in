a = 5
b = 10
c = 15

# Ambas condiciones deben ser verdaderas para que el resultado sea True
resultado = (a < b) and (b < c)  # True, porque 5 < 10 y 10 < 15

a = 5
b = 10
c = 15

# Solo una de las condiciones necesita ser verdadera para que el resultado sea True
resultado = (a < b) or (b > c)  # True, porque 5 < 10 es verdadero, aunque 10 > 15 es falso

a = 5
b = 10

# Invierte el valor de la condición
resultado = not (a < b)  # False, porque a < b es True, y not True es False

a = 5
b = 10
c = 15

# Ejemplo complejo con combinaciones de operadores lógicos
resultado = (a < b) and (b < c) or (c < a)  # True, porque (a < b) and (b < c) es True

a = 5
b = 10
c = 15

resultado = ((a < b) or (b > c)) and not (c < a)  # True
