# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
# 2 6 12 20...
n = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(n):
    suma += 2 * i + 2
    print(suma, end=" ")

print()

# b) Idem anterior para la sucesión an = n^2.
n = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(1, n + 1):
    suma += i**2
    print(suma, end=" ")

print()

# c) Idem anterior para la sucesión an = n^3 − n^2.
n = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(1, n + 1):
    suma += i**3 - i**2
    print(suma, end=" ")

print()

# d) Idem anterior para la sucesión an = 1/n^2.
n = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(1, n + 1):
    suma += 1 / (i**2)
    print(suma, end=" ")

print()

# e) ¿A qué valor se va acercando la suma del inciso anterior a medida que utilizamos
# un valor alto de n?

# La suma de la sucesión tiende a π^2/6 a medida que n aumenta, y este valor es
# aproximadamente igual a 1.64493.
