# Una función cuadrática se escribe como ax2+bx+c. La misma puede tener una, dos o ninguna
# raíz. Escribir un programa que pida al usuario los datos de la misma, es decir, a, b y c, y muestre
# todas sus raíces, o el mensaje "No tiene raíces" cuando corresponda. Recordar que las raíces están
# dadas por la fórmula (-b +- raiz(b^2-4ac))/2a.
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))


if a == 0:
    if b == 0:
        print("La ecuación no tiene solución.")
    else:
        print("La ecuación tiene una solución: x =", -c / b)
else:
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        print("La ecuación no tiene solución.")
    elif discriminante == 0:
        print("La ecuación tiene una solución: x =", -b / 2 * a)
    else:
        print(
            "La ecuación tiene dos soluciones: x1 =",
            (-b + discriminante**0.5) / 2 * a,
            "y x2 =",
            (-b - discriminante**0.5) / 2 * a,
        )
