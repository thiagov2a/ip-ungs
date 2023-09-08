# ¿Es verdad que las únicas soluciones enteras de x^((x+2)(x+3)) = 1 son x = 1 x = −2 y x = −3?.
# Hacer un programa que encuentre todas las soluciones enteras de 1 0 2 cifras tanto negativas
# como positivas.
for i in range(-99, 100):
    solucion = i ** ((i + 2) * (i + 3))
    if solucion == 1:
        print(i, "es solución")
