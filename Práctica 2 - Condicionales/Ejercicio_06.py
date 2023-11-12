# a) Escribir en papel un programa que pida al usuario dos números, y que muestre en
# pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a
# Python y por último correr el programa con los valores iniciales de las corridas y
# verificar que funciona como se esperaba.
m = int(input("Ingrese un número: "))
n = int(input("Ingrese otro número: "))

if m > n:
    print(m)
else:
    print(n)

# b) Ídem anterior pero para encontrar el menor
m = int(input("Ingrese un número: "))
n = int(input("Ingrese otro número: "))

if m < n:
    print(m)
else:
    print(n)