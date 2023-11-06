# Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
# ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
# verificar los resultados.
x = int(input("Ingrese el primer valor: "))
y = int(input("Ingrese el segundo valor: "))
z = int(input("Ingrese el tercer valor: "))

if x > y and x > z:
    print("El mayor es:", x)
else:
    if y > x and y > z:
        print("El mayor es:", y)
    else:
        print("El mayor es:", z)
