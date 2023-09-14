import math

# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
# ln(2) = 1 − 1/2 + 1/3 − 1/4 + 1/5...

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de ln(2) con esa cantidad de términos.
terminos = int(input("Ingrese la cantidad de términos para aproximarse a ln(2): "))
aproximacion = 0
signo = 1

for n in range(terminos):
    termino_actual = signo / (1 * n + 1)
    aproximacion += termino_actual
    signo *= -1

print("ln(2) ≈", aproximacion)

print()

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora? En python se puede aproximar este valor usando math.log(2)
epsilon_b = 0.1
terminos_b = 0
aproximacion_b = 0
signo_b = 1

while abs(math.log(2) - aproximacion_b) >= epsilon_b:
    termino_actual = signo_b / (1 * terminos_b + 1)
    aproximacion_b += termino_actual
    signo_b *= -1
    terminos_b += 1

print(
    "Para estar a menos de",
    epsilon_b,
    "del valor de ln(2) se necesitan al menos",
    terminos_b,
    "términos.",
)
print("ln(2) ≈", aproximacion_b)

print()


# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon_c = 0.01
terminos_c = 0
aproximacion_c = 0
signo_c = 1

while abs(math.log(2) - aproximacion_c) >= epsilon_c:
    termino_actual = signo_c / (1 * terminos_c + 1)
    aproximacion_c += termino_actual
    signo_c *= -1
    terminos_c += 1

print(
    "Para estar a menos de",
    epsilon_c,
    "del valor de ln(2) se necesitan al menos",
    terminos_c,
    "términos.",
)
print("ln(2) ≈", aproximacion_c)

print()

# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon_d = float(input("Ingrese el valor de ε (muy pequeño): "))
terminos_d = 0
aproximacion_d = 0
signo_d = 1

while abs(math.log(2) - aproximacion_d) >= epsilon_d:
    termino_actual = signo_d / (1 * terminos_d + 1)
    aproximacion_d += termino_actual
    signo_d *= -1
    terminos_d += 1

print(
    "Para estar a menos de",
    epsilon_d,
    "del valor de ln(2) se necesitan al menos",
    terminos_d,
    "términos.",
)
print("ln(2) ≈", aproximacion_d)

print()
