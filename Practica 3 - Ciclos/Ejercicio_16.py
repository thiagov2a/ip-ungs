# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
# ln(2) = 1 − 1/2 + 1/3 − 1/4 + 1/5...
# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de ln(2) con esa cantidad de términos.
terminos = int(input("Ingrese la cantidad de términos para aproximarse a ln(2): "))

suma = 0

for i in range(1, terminos + 1):
    if i % 2 == 0:
        suma -= 1 / i
    else:
        suma += 1 / i

print("ln(2) ≈", suma)

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora? En python se puede aproximar este valor usando math.log(2)
import math

epsilon = 0.1
terminos = 0
suma = 0

while abs(suma - math.log(2)) >= epsilon:
    terminos += 1
    if terminos % 2 == 0:
        suma -= 1 / terminos
    else:
        suma += 1 / terminos

print(
    f"Para estar a menos de {epsilon} del valor de ln(2) se necesitan al menos {terminos} términos."
)


# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon = 0.01
terminos = 0
suma = 0

while abs(suma - math.log(2)) >= epsilon:
    terminos += 1
    if terminos % 2 == 0:
        suma -= 1 / terminos
    else:
        suma += 1 / terminos

print(
    f"Para estar a menos de {epsilon} del valor de ln(2) se necesitan al menos {terminos} términos."
)

# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon = float(input("Ingrese el valor de ε (muy pequeño): "))
terminos = 0
suma = 0

while abs(suma - math.log(2)) >= epsilon:
    terminos += 1
    if terminos % 2 == 0:
        suma -= 1 / terminos
    else:
        suma += 1 / terminos

print(
    f"Para estar a menos de {epsilon} del valor de ln(2) se necesitan al menos {terminos} términos."
)
