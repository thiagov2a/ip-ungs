# Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
# primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
# valores de las variables y mostrarlos de mayor a menor.
num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese otro valor: "))
aux = 0

if num1 < num2:
    aux = num1
    num1 = num2
    num2 = aux

if num1 == num2:
    print("Los números son iguales")
else:
    print(num1, "es mayor que", num2)
