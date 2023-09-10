# El número 1/4π se puede aproximar de la siguiente manera:
# 1/4π = 1 − 1/3 + 1/5 − 1/7 + 1/9 - 1/11 + 1/13 - 1/15...
# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de π con esa cantidad de términos.
terminos = int(input("Ingrese la cantidad de términos para aproximarse a π: "))

bandera = False
suma = 0

for i in range(1, terminos * 2, 2):
    if bandera:
        suma -= 1 / i
    else:
        suma += 1 / i
    bandera = not bandera

aproximacion = suma * 4
print("Aproximación: π ≈", aproximacion)

print()

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora?
import math

epsilon = 0.1

bandera = False
suma = 0
i = 1

while abs(math.pi - suma * 4) >= epsilon:
    if bandera:
        suma -= 1 / i
    else:
        suma += 1 / i
    bandera = not bandera
    i += 2

print("Se necesitan al menos", i//2, "términos para estar a menos de", epsilon, "de π.")
aproximacion = suma * 4
print("Aproximación: π ≈", aproximacion)

print()

# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon = 0.01

bandera = False
suma = 0
i = 1

while abs(math.pi - suma * 4) >= epsilon:
    if bandera:
        suma -= 1 / i
    else:
        suma += 1 / i
    bandera = not bandera
    i += 2

print("Se necesitan al menos", i//2, "términos para estar a menos de", epsilon, "de π.")
aproximacion = suma * 4
print("Aproximación: π ≈", aproximacion)

print()

# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon = float(input("Ingrese el valor de ε (muy pequeño): "))

bandera = False
suma = 0
i = 1

while abs(math.pi - suma * 4) >= epsilon:
    if bandera:
        suma -= 1 / i
    else:
        suma += 1 / i
    bandera = not bandera
    i += 2

print("Se necesitan al menos", i//2, "términos para estar a menos de", epsilon, "de π.")
aproximacion = suma * 4
print("Aproximación: π ≈", aproximacion)
