# Determinar cuántos segundos tiene una hora, y cuántos tiene un día.
segundos_hora = 3600
segundos_dia = 86400

# Escribir una expresión matemática que transforme un lapso de tiempo expresado en segundos a uno
# expresado en minutos.
minutos = segundos_hora / 60

# Escribir otra para transformar a horas y una última que transforme a días.
horas = segundos_hora / 3600
dias = segundos_dia / 86400


# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos
# minutos son, así como también cuantas horas y cuantos días.

segundos = int(input("Ingrese la cantidad de segundos: "))

minutos = segundos / 60

horas = segundos / 3600

dias = segundos / 86400

print("La cantidad de segundos ingresada es: ", segundos)
print("La cantidad de minutos ingresada es: ", minutos)
print("La cantidad de horas ingresada es: ", horas)
print("La cantidad de dias ingresada es: ", dias)
