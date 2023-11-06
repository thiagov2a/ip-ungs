# Ejercicio 2
# Se desea hacer una función llamada pagan_esto() para una veterinaria, que devuelve una lista con los montos que
# tendrá que pagar cada dueño por la atención a su mascota. La veterinaria cobra una tarifa dependiendo de qué tipo
# de mascota tengas, si tenes un gato pagas $500, si tenes un perro pagas $700, si tenes un chanchito pagas $2000.
# Además la clínica hace un descuento del 50% si estás asociado al AALM "Asociación Amar a los Michis".

# Aclaración: Ya suponemos que las listas de dueños y mascotas están correspondidas.

# dueños(): Devuelve una lista con todos los dueños.
# mascotas(): Devuelve una lista con el tipo de mascota.
# asociado(dueño): Recibe como parámetro al dueño y si está asociado devuelve True, en caso contrario devuelve False.

##################SOLO PARA PROBAR###################

import random


def dueños():
    return ["Thiago", "Santiago", "Franco", "Nicolás"]


def mascotas():
    return ["gato", "chanchito", "perro", "perro"]


def asociado(dueño):
    rand = random.randint(0, 1)
    return True if rand == 1 else False


###################SOLO PARA PROBAR#################


def pagan_esto():
    montos = []
    lista_dueños = dueños()
    lista_mascotas = mascotas()

    for i in range(len(lista_dueños)):
        monto = 0
        dueño = lista_dueños[i]
        mascota = lista_mascotas[i]

        if mascota == "gato":
            monto += 500

        if mascota == "perro":
            monto += 700

        if mascota == "chanchito":
            monto += 2000

        if asociado(dueño):
            monto *= 0.5

        montos.append(monto)

    return montos


print(pagan_esto())
