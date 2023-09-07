# Escribe un programa que pida los coeficientes de una ecuación de primer grado (ax + b = 0)
# y escriba la solución. Recuerda que una ecuación de primer grado puede no tener solución, tener
# una solución única, o que todos los números reales sean solución.
a = float(input("Ingrese el coeficiente a: "))  
b = float(input("Ingrese el coeficiente b: "))

if a == 0:
    if b == 0:
        print("La ecuación tiene soluciones infinitas (todos los números reales son solución).")
    else:
        print("La ecuación no tiene solución.")
else:
    print("La ecuación tiene una solución: x =", -b/a)