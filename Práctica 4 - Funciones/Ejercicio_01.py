# Hacer un programa para cada inciso que pida al usuario un número decimal x y muestre por
# pantalla el resultado de evaluar las siguientes fórmulas:
# a) √x
# b) |x|
# c) |x − 3|
# d) √|x − 5|
import math

x = float(input("Ingrese un número decimal: "))

print("√x =", math.sqrt(x))
print("|x| =", abs(x))
print("|x - 3| =", abs(x - 3))
print("√|x - 5| =", math.sqrt(abs(x - 5)))
