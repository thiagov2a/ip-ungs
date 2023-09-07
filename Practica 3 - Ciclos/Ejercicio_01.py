# a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
# (1, 2, 3, 4 y 5).
for i in range(1, 6):
    if i == 5:
        print(i)
    else:
        print(i, end=", ")

# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# primeros n números naturales (1, 2, · · · , n).
n = int(input("Ingrese un número entero positivo: "))

for i in range(1, n + 1):
    if i == n:
        print(i)
    else:
        print(i, end=", ")
