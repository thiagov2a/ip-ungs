# Hacer un programa que solicite dos cadenas, nombre y apellido y arme el legajo de estudiantes
# de la universidad de la siguiente manera:
# Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3
# primeras letras del apellido y por ultimo la primera y ultima del nombre.
# Por ejemplo:
# JavierRodriguez 38946702
# Legajo: 389_rodjr

# Ingreso de datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Pedimos el DNI en String para poder recorrerlo
dni = input("Ingrese su DNI: ")

# Definimos la variable legajo
legajo = ""

# Recorremos 'dni' y le asignamos a lejago los primeros 3 caracteres
cont = 0
for char in dni:
    if cont != 3:
        legajo += char
        cont += 1

# Agregamos el símbolo barra baja al legajo
legajo += "_"

# Recorremos 'apellido' y le asignamos a lejago los primeros 3 caracteres
cont = 0
for char in apellido:
    if cont != 3:
        legajo += char.lower()
        cont += 1

# Recorremos 'nombre' y le asignamos a legajo el primer y último carácter
i = 0
for char in nombre:
    if i == 0 or i == len(nombre) - 1:
        legajo += char.lower()
    i += 1

print(legajo)
