# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
# 11 salteando de a 2 elementos (5, 7, 9 y 11)
for i in range(5, 12, 2):
    if i == 11:
        print(i)
    else:
        print(i, end=", ")

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
# usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
# 2, 5, 8, 11, 14.
m = int(input("Ingrese un número inicial para el rango: "))
n = int(input("Ingrese otro número final para el rango: "))

if n < m:
    for i in range(m, n - 1, -3):
        if i - 3 < n:
            print(i)
        else:
            print(i, end=", ")
else:
    for i in range(m, n + 1, 3):
        if i + 3 > n:
            print(i)
        else:
            print(i, end=", ")

# c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
# luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
# ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
# el programa deberá mostrar 2, 6, 10, 14.
m = int(input("Ingrese un número inicial para el rango: "))
n = int(input("Ingrese otro número final para el rango: "))
p = int(input("Ingresa un número para el paso del rango: "))

if p <= 0:
    print("El paso debe ser un número positivo.")
else:
    if n < m:
        for i in range(m, n - 1, -p):
            if i - p < n:
                print(i)
            else:
                print(i, end=", ")
    else:
        for i in range(m, n + 1, p):
            if i + p > n:
                print(i)
            else:
                print(i, end=", ")
