# Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
# mayor que el segundo o viceversa.
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    print(num1, "es mayor que", num2)
elif num2 > num1:
    print(num2, "es mayor que", num1)
else:
    print("Los números son iguales")
