# Ejercicio 1

rubros = ["librerías", "diversión", "indumentaria", "almacenes", "cines"]
dias = ["lunes", "miércoles", "lunes", "jueves", "sábado"]
porcentajes = [40, 30, 25, 20, 15]


def descuentos(dia, monto):
    for i in range(len(dias)):
        if dias[i] == dia:
            resultado = monto * (porcentajes[i] / 100)

            print(
                "Tenés descuentos en",
                rubros[i],
                "con un",
                porcentajes[i],
                "%, se te devuelve $",
                resultado,
            )


dia = input("¿Qué día de la semana tenés pensado ir a comprar? ")
monto = int(input("¿Cuánto dinero estas dispuesto a pagar? "))

descuentos(dia, monto)


# Ejercicio 3


# def controlBodega():
#     bodegasHabilitadas = bodegasHabilitadas()

#     listaBodegas = []
#     listaCondicion = []

#     for i in range(len(bodegasHabilitadas)):
#         bodega = bodegasHabilitadas[i]
#         temperatura = controlTemp(bodega)

#         if temperatura < 12 or temperatura > 16:
#             listaBodegas.append(bodega)
#             listaCondicion.append(temperatura)

#     enviarAlerta(listaBodegas, listaCondicion)
