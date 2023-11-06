import math

# Escribir un programa que solicite al usuario un número positivo y aproxime el valor del número
# e de la siguiente manera: (ejemplo para 7 términos)
# 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6!
terminos = int(input("Ingrese un número de términos para aproximar a 'e': "))
factorial = 1
aproximacion = 0

for i in range(terminos):
    aproximacion += 1 / factorial
    factorial *= i + 1

print("Aproximación de 'e' =", aproximacion)
print()

# a) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora?
epsilon = 0.1
factorial = 1
aproximacion = 0
terminos = 0

while abs(math.e - aproximacion) >= epsilon:
    aproximacion += 1 / factorial
    factorial *= terminos + 1
    terminos += 1

print("Aproximación de 'e' =", aproximacion, "con", terminos, "términos")
print()

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon = 0.01
factorial = 1
aproximacion = 0
terminos = 0

while abs(math.e - aproximacion) >= epsilon:
    aproximacion += 1 / factorial
    factorial *= terminos + 1
    terminos += 1

print("Aproximación de 'e' =", aproximacion, "con", terminos, "términos")
print()

# c) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon = float(input("Ingrese el valor de ε (muy pequeño) para aproximar a 'e': "))
factorial = 1
aproximacion = 0
terminos = 0

while abs(math.e - aproximacion) >= epsilon:
    aproximacion += 1 / factorial
    factorial *= terminos + 1
    terminos += 1

print("Aproximación de 'e' =", aproximacion, "con", terminos, "términos")
