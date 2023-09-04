# a) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores de n.
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, "es divisor de", n)

# b) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores pares de n.
n = int(input("Ingrese un número positivo: "))

for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 0:
        print(i, "es divisor de", n)

# c) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla la cantidad de divisores de n.
n = int(input("Ingrese un número positivo: "))

suma = 0
for i in range(1, n + 1):
    if n % i == 0:
        suma += 1

print("La cantidad de divisores de", n, "es de", suma)

# d) Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla la suma de los divisores de n.
n = int(input("Ingrese un número positivo: "))

suma = 0
for i in range(1, n + 1):
    if n % i == 0:
        suma += i

print("La suma de los divisores de", n, "es de", suma)

# e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los primeros c divisores de n.
n = int(input("Ingrese un número positivo: "))
c = int(input("Ingrese la cantidad de los primeros divisores a obtener: "))

for i in range(1, n + 1):
    if n % i == 0 and c != 0:
        print(i, "es divisor de", n)
        c -= 1

# f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los últimos c divisores de n.
n = int(input("Ingrese un número positivo: "))
c = int(input("Ingrese la cantidad de los ultimos divisores a obtener: "))

for i in range(n, 0, -1):
    if n % i == 0 and c != 0:
        print(i, "es divisor de", n)
        c -= 1
