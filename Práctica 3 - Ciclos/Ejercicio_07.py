# Hacer todos los ejercicios anteriores de nuevo, pero esta vez utilizando la sentencia while en
# lugar de for. De haberlos hecho con while, rehacerlos utilizando for.

# Ejercicio 1
# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
# (1, 2, 3, 4 y 5).
i = 1

while i <= 5:
    if i == 5:
        print(i)
    else:
        print(i, end=", ")
    i += 1

# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).
n = int(input("Ingrese un número entero positivo: "))

i = 1

while i <= n:
    if i == n:
        print(i)
    else:
        print(i, end=", ")
    i += 1

# Ejercicio 2
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
# 7 (4, 5, 6 y 7).
i = 4

while i <= 7:
    if i == 7:
        print(i)
    else:
        print(i, end=", ")
    i += 1

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¿Qué pasa
# si n es menor que m?
m = int(input("Ingrese un número: "))
n = int(input("Ingrese otro número: "))

i = m

if n < m:
    while i >= n:
        if i == n:
            print(i)
        else:
            print(i, end=", ")
        i -= 1
else:
    while i <= n:
        if i == n:
            print(i)
        else:
            print(i, end=", ")
        i += 1


# Ejercicio 3
# a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
# siguen al 10 (11, 12, · · · , 15).
print("Los 5 números naturales que le siguen a 10 son:")

i = 11

while i <= 15:
    if i == 15:
        print(i)
    else:
        print(i, end=", ")
    i += 1

# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
n = int(input("Ingrese un número entero positivo: "))

print("Los 5 números naturales que le siguen a", n, "son:")

i = n + 1

while i <= n + 5:
    if i == n + 5:
        print(i)
    else:
        print(i, end=", ")
    i += 1

# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
n = int(input("Ingrese un número entero positivo: "))
c = int(input("Ingrese otro número entero positivo (cantidad de números a mostrar): "))

print("Los", c, "números naturales que le siguen a", n, "son:")

i = n + 1

while i <= n + c:
    if i == n + c:
        print(i)
    else:
        print(i, end=", ")
    i += 1

# Ejercicio 4
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
# 11 salteando de a 2 elementos (5, 7, 9 y 11)
i = 5

while i <= 11:
    if i == 11:
        print(i)
    else:
        print(i, end=", ")
    i += 2

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
# usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
# 2, 5, 8, 11, 14.
m = int(input("Ingrese un número inicial para el rango: "))
n = int(input("Ingrese otro número final para el rango: "))

i = m

if n < m:
    while i >= n:
        if i - 3 < n:
            print(i)
        else:
            print(i, end=", ")
        i -= 3
else:
    while i <= n:
        if i + 3 > n:
            print(i)
        else:
            print(i, end=", ")
        i += 3


# c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
# luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
# ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14.
m = int(input("Ingrese un número inicial para el rango: "))
n = int(input("Ingrese otro número final para el rango: "))
p = int(input("Ingresa un número para el paso del rango: "))

i = m

if p <= 0:
    print("El paso debe ser un número positivo.")
else:
    if n < m:
        while i >= n:
            if i - p < n:
                print(i)
            else:
                print(i, end=", ")
            i -= p
    else:
        while i <= n:
            if i + p > n:
                print(i)
            else:
                print(i, end=", ")
            i += p

# Ejercicio 5
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el
# 3 (8, 7, 6, 5, 4, 3).
i = 8

while i >= 3:
    if i == 3:
        print(i)
    else:
        print(i, end=", ")
    i -= 1

# Ejercicio 6
# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta
# el 6 pero salteando de a tres (15, 12, 9, 6).
i = 15

while i >= 6:
    if i - 3 < 6:
        print(i)
    else:
        print(i, end=", ")
    i -= 3
