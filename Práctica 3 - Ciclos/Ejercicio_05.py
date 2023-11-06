# a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el
# 3 (8, 7, 6, 5, 4, 3).
for i in range(8, 2, -1):
    if i == 3:
        print(i)
    else:
        print(i, end=", ")
