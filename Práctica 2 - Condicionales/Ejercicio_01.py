# Este programa chequea una serie de condiciones para los tres valores ingresados por el usuario.
# Correrlo tal cual está en Python. Luego reemplazar donde dice True por una expresión lógica
# que sea True o False según corresponda, en lugar de siempre True como ahora.
a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese un número entero: "))
c = int(input("Ingrese un número entero: "))

print("Usted ingresó los valores:", a, b, c)
print(a, "es mayor que", b, ":", a > b)
print(a, "y", b, "son iguales:", a == b)
print(a, "es el mayor de todos:", a > b and a > c)
print(b, "es el menor de todos:", b < a and b < c)
print(a, "es mayor que alguno de los otros dos:", a > b or a > c)
print(a, "es menor o igual que alguno de los otros dos:", a <= b or a <= c)
print("Los tres números son iguales:", a == b and a == c and b == c)
print("Los tres numeros son distintos:", a != b and a != c and b != c)
print(a, "es par:", a % 2 == 0)
print("Alguno es par:", a % 2 == 0 or b % 2 == 0 or c % 2 == 0)
print("Ninguno es par:", a % 2 != 0 and b % 2 != 0 and c % 2 != 0)
print("Todos son pares:", a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
print(a, "es múltiplo de 3:", a % 3 == 0)
print(a, "es múltiplo de 3 y de 5:", a % 3 == 0 and a % 5 == 0)
print(a, "es múltiplo de 3 y par:", a % 3 == 0 and a % 2 == 0)
print(a, "-", b, "da un número positivo:", (a - b) > 0)
print(a, "-", b, "da un número par positivo:", (a - b) > 0 and (a - b) % 2 == 0)
