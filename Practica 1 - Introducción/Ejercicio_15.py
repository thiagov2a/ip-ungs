# Un vendedor recibe un sueldo base de $42000 más un 10 % extra del total de sus ventas, el vendedor
# desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en
# cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada una
# de las ventas del mes e indique cuál será el sueldo final del vendedor. Por ejemplo, si realizó una venta
# de $12000, otra de $6000 y una tercera de $22000 su sueldo será de $46000
sueldo_base = 42000

venta_1 = int(input("Ingrese el monto de la primera venta: "))
venta_2 = int(input("Ingrese el monto de la segunda venta: "))
venta_3 = int(input("Ingrese el monto de la tercera venta: "))

comision = (venta_1 + venta_2 + venta_3) * 0.1

sueldo_final = sueldo_base + comision

print("El sueldo final del vendedor es de:", sueldo_final)
