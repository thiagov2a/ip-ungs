# Hacer en pseudocódigo y luego un programa que calcule el importe que se le facturará a un
# cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa
# fija de 480 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra
# a 25,5 pesos el KW, además se agregan $78 de impuestos. Se leen los valores del medidor al
# comienzo y al fin del período.
kw_inicial = float(input("Ingrese el valor del medidor inicial: "))
kw_final = float(input("Ingrese el valor del medidor final: "))

kw_consumidos = kw_final - kw_inicial

if kw_consumidos <= 200:
    importe = 480 + 78
else:
    importe = 480 + 78 + (kw_consumidos - 200) * 25.5
    
print("El importe a pagar es de:", importe)