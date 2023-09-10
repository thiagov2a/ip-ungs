# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
# 6...
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    print(2 * i, end=" ")

print()

# b) Idem anterior para la sucesión an = 2n − 1.
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    print(2 * i - 1, end=" ")

print()

# c) Idem anterior para la sucesión an = n^2.
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    print(i**2, end=" ")

print()

# d) Idem anterior para la sucesión an = n^3 − n^2.
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    print(i**3 - i**2, end=" ")

print()

# e) Idem anterior para la sucesión an = 1/n2.
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    print(1 / (i**2), end=" ")

print()
