# a) Escribir un programa que pida al usuario un número n y muestre una línea de n
# asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:
# ********
n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    print("*", end="")
print()

# b) Escribir un programa que pida al usuario un número n y muestre n líneas de
# 1, 2, 3, ...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá
# mostrar:
# *
# **
# ***
# ****
# *****
n = int(input("Ingrese un número: "))

for i in range(n):
    for j in range(1 * i + 1):
        print("*", end="")
    print()

# c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2n − 1
# asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:
# *
# ***
# *****
# *******
# *********
n = int(input("Ingrese un número: "))

for i in range(n):
    for j in range(2 * i + 1):
        print("*", end="")
    print()
