# Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
# El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
# b el intermedio y en c el mayor (es decir, ordenará los valores).
a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))
c = int(input("Ingrese un valor para c: "))

if a > b:
    aux = a
    a = b
    b = aux

if b > c:
    aux = b
    b = c
    c = aux

if a > b:
    aux = a
    a = b
    b = aux

print("a:", a)
print("b:", b)
print("c:", c)
