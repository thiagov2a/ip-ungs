# Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
# pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n.
n = int(input("Ingresa un número: "))

producto = 1

for i in range(1, n + 1):
    producto *= i

print("El producto de los números entre 1 y", n, "es:", producto)
