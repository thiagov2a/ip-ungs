# Se tiene la siguiente lista con DNIs de personas.
dni_1 = 30612453
dni_2 = 23763290
dni_3 = 21448503
dni_4 = 34582048
dni_5 = 15364857
# Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno
# de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.
DNI = int(input("Ingrese un número de DNI: "))

if DNI == dni_1 or DNI == dni_2 or DNI == dni_3 or DNI == dni_4 or DNI == dni_5:
    print("El número de DNI ingresado se encuentra en la lista")
else:
    print("El número de DNI ingresado NO se encuentra en la lista")
