# a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
# menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
# 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
n = int(input("Ingrese un número: "))

potencia = 1

while potencia < n:
    print(potencia, end=" ")
    potencia *= 2

# b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
# 16 32.
n = int(input("Ingrese un número: "))

potencia = 1

for i in range(n):
    print(potencia, end=" ")
    potencia *= 2

# c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
# 256. Es decir, 1^1 2^2 3^3 4^4.
n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    potencia = i**i
    print(potencia, end=" ")
