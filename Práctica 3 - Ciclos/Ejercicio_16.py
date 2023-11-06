import math

# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
# ln(2) = 1 − 1/2 + 1/3 − 1/4 + 1/5...

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de ln(2) con esa cantidad de términos.
terminos = int(input("Ingrese un número de términos para aproximar a ln(2): "))
aproximacion = 0
signo = 1

for i in range(terminos):
    aproximacion += signo / (1 * i + 1)
    signo *= -1

print("Aproximación de ln(2) =", aproximacion)
print()

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora? En python se puede aproximar este valor usando math.log(2)
epsilon = 0.1
terminos = 0
aproximacion = 0
signo = 1

while abs(math.log(2) - aproximacion) >= epsilon:
    aproximacion += signo / (1 * terminos + 1)
    signo *= -1
    terminos += 1

print("Aproximación de ln(2) =", aproximacion, "con", terminos, "términos")
print()


# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon = 0.01
terminos = 0
aproximacion = 0
signo = 1

while abs(math.log(2) - aproximacion) >= epsilon:
    aproximacion += signo / (1 * terminos + 1)
    signo *= -1
    terminos += 1

print("Aproximación de ln(2) =", aproximacion, "con", terminos, "términos")
print()

# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon = float(input("Ingrese el valor de ε (muy pequeño) para aproximar a ln(2): "))
terminos = 0
aproximacion = 0
signo = 1

while abs(math.log(2) - aproximacion) >= epsilon:
    aproximacion += signo / (1 * terminos + 1)
    signo *= -1
    terminos += 1

print("Aproximación de ln(2) =", aproximacion, "con", terminos, "términos")
