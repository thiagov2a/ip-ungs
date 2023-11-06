import math

# El número 1/4π se puede aproximar de la siguiente manera:
# 1/4π = 1 − 1/3 + 1/5 − 1/7 + 1/9 - 1/11 + 1/13 - 1/15...

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de π con esa cantidad de términos.
terminos = int(input("Ingrese un número de términos para aproximar a π: "))
aproximacion = 0
signo = 1

for i in range(terminos):
    aproximacion += signo / (2 * i + 1)
    signo *= -1

aproximacion *= 4

print("Aproximación de π =", aproximacion)
print()

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora?
epsilon = 0.1
aproximacion = 0
signo = 1
terminos = 0

while abs(math.pi - aproximacion * 4) >= epsilon:
    aproximacion += signo / (2 * terminos + 1)
    signo *= -1
    terminos += 1

aproximacion *= 4

print("Aproximación de π =", aproximacion, "con", terminos, "términos")
print()

# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon = 0.01
aproximacion = 0
signo = 1
terminos = 0

while abs(math.pi - aproximacion * 4) >= epsilon:
    aproximacion += signo / (2 * terminos + 1)
    signo *= -1
    terminos += 1

aproximacion *= 4

print("Aproximación de π =", aproximacion, "con", terminos, "términos")
print()

# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon = float(input("Ingrese el valor de ε (muy pequeño) para aproximar a π: "))
aproximacion = 0
signo = 1
terminos = 0

while abs(math.pi - aproximacion * 4) >= epsilon:
    aproximacion += signo / (2 * terminos + 1)
    signo *= -1
    terminos += 1

aproximacion *= 4

print("Aproximación de π =", aproximacion, "con", terminos, "términos")
