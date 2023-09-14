import math

# El número 1/4π se puede aproximar de la siguiente manera:
# 1/4π = 1 − 1/3 + 1/5 − 1/7 + 1/9 - 1/11 + 1/13 - 1/15...

# a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y
# que muestre la aproximación de π con esa cantidad de términos.
terminos = int(input("Ingrese la cantidad de términos para aproximarse a π: "))
aproximacion = 0
signo = 1

for n in range(terminos):
    termino_actual = signo / (2 * n + 1)
    aproximacion += termino_actual
    signo *= -1

aproximacion *= 4

print("π ≈", aproximacion)

print()

# b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que
# da la calculadora?
epsilon_b = 0.1
terminos_b = 0
aproximacion_b = 0
signo_b = 1

while abs(math.pi - aproximacion_b * 4) >= epsilon_b:
    termino_actual = signo_b / (2 * terminos_b + 1)
    aproximacion_b += termino_actual
    signo_b *= -1
    terminos_b += 1

aproximacion_b *= 4

print(
    "Se necesitan al menos",
    terminos_b // 2,
    "términos para estar a menos de",
    epsilon_b,
    "de π.",
)
print("π ≈", aproximacion_b)

print()

# c) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que
# da la calculadora?
epsilon_c = 0.01
terminos_c = 0
aproximacion_c = 0
signo_c = 1

while abs(math.pi - aproximacion_c * 4) >= epsilon_c:
    termino_actual = signo_c / (2 * terminos_c + 1)
    aproximacion_c += termino_actual
    signo_c *= -1
    terminos_c += 1

aproximacion_c *= 4

print(
    "Se necesitan al menos",
    terminos_c // 2,
    "términos para estar a menos de",
    epsilon_c,
    "de π.",
)
print("π ≈", aproximacion_c)

print()

# d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar,
# pida al usuario un número decimal ε (muy chico) y calcule la suma hasta que el
# error comparado con el valor de la calculadora sea menor que ε
epsilon_d = float(input("Ingrese el valor de ε (muy pequeño): "))
terminos_d = 0
aproximacion_d = 0
signo_d = 1

while abs(math.pi - aproximacion_d * 4) >= epsilon_d:
    termino_actual = signo_d / (2 * terminos_d + 1)
    aproximacion_d += termino_actual
    signo_d *= -1
    terminos_d += 1

aproximacion_d *= 4

print(
    "Se necesitan al menos",
    terminos_d // 2,
    "términos para estar a menos de",
    epsilon_d,
    "de π.",
)
print("π ≈", aproximacion_d)
