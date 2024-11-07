x = 10
y = 20

# if básico
if x < y:
    print("x es menor que y")

# if con else
if x > y:
    print("x es mayor que y")
else:
    print("x no es mayor que y")

# if con múltiples elif y else
if x == y:
    print("x es igual a y")
elif x < y:
    print("x es menor que y")
else:
    print("x es mayor que y")

# Uso de operadores lógicos
if x < y and x > 5:
    print("x es menor que y y mayor que 5")

# Condición en una sola línea (operador ternario)
resultado = "Positivo" if x > 0 else "Negativo o Cero"
print(resultado)
