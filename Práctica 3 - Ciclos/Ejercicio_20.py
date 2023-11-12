# a) Escribir un programa que permita al usuario elegir un número m y un n y
# muestre todos los pares de números que se pueden formar con los números que están
# entre ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberá mostrar
# 4 4
# 4 5
# 4 6
# 5 4
# 5 5
# 5 6
# 6 4
# 6 5
# 6 6
m = int(input("Ingrese un número: "))
n = int(input("Ingrese otro número: "))

for i in range(m, n + 1):
    for j in range(m, n + 1):
        print(i, j)

# b) Cambiar el programa para que use sólo un ciclo en vez de dos.
diferencia = abs(m - n) + 1
vueltas = diferencia**2
aux = m

for i in range(vueltas):
    if i % diferencia == 0:
        n = aux
        m += 1
    print(m - 1, n)
    n += 1
