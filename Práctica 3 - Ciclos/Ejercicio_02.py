# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
# 7 (4, 5, 6 y 7).
for i in range(4, 8):
    if i == 7:
        print(i)
    else:
        print(i, end=", ")

# b) Hacer un programa que permita al usuario elegir un número m y un n y luego
# muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¿Qué pasa
# si n es menor que m?
m = int(input("Ingrese un número: "))
n = int(input("Ingrese otro número: "))

if n < m:
    for i in range(m, n - 1, -1):
        if i == n:
            print(i)
        else:
            print(i, end=", ")
else:
    for i in range(m, n + 1):
        if i == n:
            print(i)
        else:
            print(i, end=", ")
