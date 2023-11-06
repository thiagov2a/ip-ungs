# Un ciudadano argentino está exento de votar en estos casos:
# Tiene más de 70 años
# Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
# Suponiendo que las variables edad y distancia representan la edad y la distancia del
# ciudadano, escribir la expresión lógica que representa esta situación.
edad = 19
distancia = 100

edad > 70 or (edad >= 18 and distancia > 500)
