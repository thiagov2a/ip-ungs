# a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
# siguen al 10 (11, 12, · · · , 15).
print("Los 5 números naturales que le siguen a 10 son:")

for i in range(11, 16):
    if i == 15:
        print(i)
    else:
        print(i, end=", ")

# b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
# 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
n = int(input("Ingrese un número entero positivo: "))

print("Los 5 números naturales que le siguen a", n, "son:")

for i in range(n + 1, n + 6):
    if i == n + 5:
        print(i)
    else:
        print(i, end=", ")

# c) Hacer un programa que permita al usuario elegir un número n y un número c, y
# luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
n = int(input("Ingrese un número entero positivo: "))
c = int(input("Ingrese otro número entero positivo (cantidad de números a mostrar): "))

print("Los", c, "números naturales que le siguen a", n, "son:")

for i in range(n + 1, n + c + 1):
    if i == n + c:
        print(i)
    else:
        print(i, end=", ")
