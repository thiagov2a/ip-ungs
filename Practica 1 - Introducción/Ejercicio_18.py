# Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla
# la cantidad de días, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461 segundos
# el programa debe mostrar por pantalla: 1 día 0 horas 1 minuto 1 segundo.
segundos = int(input("Ingrese la cantidad de segundos: "))

dias = segundos // 86400
segundos %= 86400

horas = segundos // 3600
segundos %= 3600

minutos = segundos // 60
segundos %= 60

print(dias, "día(s)", horas, "hora(s)", minutos, "minuto(s)", segundos, "segundo(s)")
