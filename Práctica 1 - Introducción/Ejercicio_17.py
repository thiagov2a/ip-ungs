# La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
# billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada
# denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda:
# El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.
dinero = int(input("Ingrese la cantidad de dinero a extraer: "))

billete_100 = dinero // 100
dinero %= 100

billete_50 = dinero // 50
dinero %= 50

billete_20 = dinero // 20
dinero %= 20

billete_10 = dinero // 10
dinero %= 10

billete_5 = dinero // 5
dinero %= 5

billete_1 = dinero

print(billete_100, "billetes de 100")
print(billete_50, "billetes de 50")
print(billete_20, "billetes de 20")
print(billete_10, "billetes de 10")
print(billete_5, "billetes de 5")
print(billete_1, "billetes de 1")
