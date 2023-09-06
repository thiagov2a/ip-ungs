# Un profesor clasifica las notas de sus alumnos de la siguiente manera:
# 1-3 Reprobado
# 4-6 Debe rendir examen final
# 7-10 Eximido
# a) Escribir un programa que indique la clasificación de una nota.
nota = int(input("Ingrese la nota: "))

if nota < 1 or nota > 10:
    print("La nota ingresada no es válida")
else:
    if nota < 4:
        print("Reprobado")
    elif nota < 7:
        print("Debe rendir examen final")
    else:
        print("Eximido")
    
# b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación
# del mismo.
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

if (nota1 < 1 or nota1 > 10) or (nota2 < 1 or nota2 > 10) or (nota3 < 1 or nota3 > 10):
    print("Las notas ingresadas no son válidas")
else:
    promedio = (nota1 + nota2 + nota3) / 3
    
    if promedio < 4:
        print("Reprobado")
    elif promedio < 7:
        print("Debe rendir examen final")
    else:
        print("Eximido")
