# Compuerta lógica AND
# 1 | 1 -> True
# 1 | 0 -> False
# 0 | 1 -> False
# 0 | 0 -> False

# Compuerta lógica OR
# 1 | 1 -> True
# 1 | 0 -> True
# 0 | 1 -> True
# 0 | 0 -> False

# Compuerta lógica NOT
# 1 -> 0 | True -> False
# 0 -> 1 | False -> True

# Ejercicio 1
# a. Sabiendo que sensor es una variable de tipo entero:
sensor = 0
# Decir para qué valores de la variable sensor es verdadela la siguiente condición:
sensor == 0 or (sensor > 9 and sensor < 21)

# Sol = {0} U (9, 21)

# b. Si se tiene las siguiente variable booleanas:
w = True
v = False
z = False
# ¿Qué rama del condicional se ejecutará? if not(w and v) or z:

not (w and v) or z
not (False) or False
True or False
True
# La rama que cumple la condición es not(w and v) ya que la compuerta lógica and no
# se cumple al ser w y v distintos, el False en un not(False) -> True.

# c. ¿Qué resultado imprimirá en pantalla al terminar el siguiente ciclo?
valor = 10
for i in range(-3, 1):  # [-3, 1)
    valor = valor + i
print(valor * 2)

# iteración | valor |  i  | valor = valor + i
# 1         | 10    | -3  | 10 + (-3) = 7
# 2         | 7     | -2  | 7 + (-2) = 5
# 3         | 5     | -1  | 5 + (-1) = 4
# 4         | 4     | 0   | 4 + 0 = 4

# print(valor * 2) -> 4 * 2 = 8
# El programa imprimirá al final del ciclo el valor de 8

# Ejercicio 2
# Dado el siguiente programa:
numero = int(input("Ingrese un número entero mayor o igual a diez: "))  # Línea 10
while numero < 10:  # Línea 20
    numero = int(input("Ingrese un número entero mayor o igual a diez:"))  # Línea 30
for i in range(10, numero + 1):  # Línea  40
    if i % 5 == 0:  # Línea 50
        print(i)  # Línea 60

# a. ¿Qué está escribiendo el programa?

# El programa escribe los valores de i divisores de 5, estos mayores o iguales a 10.

# b. ¿Para que sirven las líneas 20 y 30 del programa?

# Las líneas 20 y 30 sirven para pedir nuevamente el valor de la variable numero en
# caso de que el mismo sea menor a 10, esto se repetira hasta que numero sea mayor o
# igual a 10.

# c. Si un usuario ingresa como número un 22, ¿qué escribiría el programa?
# ¿y si se ingresara 24?

# En caso de que 'numero = 22' el programa imprimirá la siguiente salida:
# 10
# 15
# 20
# En caso de que 'numero = 24' el programa imprimirá los valores anteriores.

# d. Agregar las líneas de código necesarias al programa para que cuente la cantidad de
# números que cumplen con la guarda de la línea 50

numero = int(input("Ingrese un número entero mayor o igual a diez: "))  # 10
while numero < 10:  # 20
    numero = int(input("Ingrese un número entero mayor o igual a diez:"))  # 30
contador = 0  # 40
for i in range(10, numero + 1):  # 50
    if i % 5 == 0:  # 60
        contador += 1  # 70 - Incrementa el contador si la condición se cumple
        print(i)  # 80
print("Cantidad de números que cumplen la guarda:", contador)  # 90

# En caso de querer contar la cantidad de números que cumplen con la condición, agregamos
# las líneas 40, 70 y 90. En primer lugar, instanciamos un contador en cero; luego,
# le sumamos 1 al contador en caso de que la condición en la línea 60 se cumpla.
# Finalmente, imprimimos el valor del contador.

# Ejercicio 3
# Hacer un programa que solicite al usuario un color y un animal, y genere una cadena
# nueva de la siguiente forma: se debe colocar al animal ingresado al revés, poner luego
# un carater asterisco y después el color reemplazando, si hubiera, las apariciones de
# las siguientes vocales: "o" por "$" y "a" por "@". Ejemplo: color: blanco, animal:
# tigre -> la nueva cadena será: ergit*bl@nc$

color = input("Ingrese un color: ")
animal = input("Ingrese un animal: ")
cadena_nueva = ""

for char in animal:
    cadena_nueva = char + cadena_nueva

cadena_nueva += "*"

for char in color:
    if char == "o" or char == "O":
        cadena_nueva += "$"
    elif char == "a" or char == "A":
        cadena_nueva += "@"
    else:
        cadena_nueva += char

print("Cadena nueva:", cadena_nueva)

# Ejercicio 4
# ¿Qué imprimen las siguientes líneas de código?

# a.
print(3**2 - 3 * 2)

# (3**2) -> 9
# (- 3 * 2) -> - 6
# 9 - 6 = 3
# El programa imprimirá 3

# b.
print(12 % 5)

# Observación: El operador de módulo % se utiliza para obtener el residuo de una división
# entre dos números. Por ejemplo, 10 % 3 es igual a 1, ya que 10 dividido por 3 es 3
# con un residuo de 1.

# 12 % 5 -> 2
# El programa imprimirá 2

# c.
print(len("1er Parcial"))

# Observación: La función len() te permite saber cuántos elementos hay en una cadena
# de texto. Por ejemplo, len("Hola") te dará 4, porque hay 4 letras en la palabra "Hola".

# len("1er Parcial") -> 11
# El programa imprimirá 11

# d.
print("$+#" * 3)

# Observación: La operación * 3 indica que la cadena "$+#" se repetirá tres veces
# consecutivas.

# El programa imprimirá $+#$+#$+#

# Ejercicio 5
# Dadas dos cadenas de caracteres (cadena_1 y cadena_2), hacer un programa que arme una
# nueva cadena tal que los primeros caracteres sean los de posiciones impares de cadena_1
# y los últimos de posiciones pares de cadena_2. Por ejemplo: cadena_1 = "Hola" y
# cadena_2 = "leones" debe armar la nueva cadena "Hlens" (los dos primeros caracteres son
# el primero y el tercero de cadena_1 y los tres últimos el segundo, cuarto y sexto de
# cadena_2).

cadena_1 = input("Ingrese una palabra: ")
cadena_2 = input("Ingrese otra palabra: ")
cadena_nueva = ""

contador = 1
for char in cadena_1:
    if contador % 2 != 0:  # Concición impar
        cadena_nueva += char
    contador += 1

contador = 1
for char in cadena_2:
    if contador % 2 == 0:  # Concición par
        cadena_nueva += char
    contador += 1

print("La nueva cadena es", cadena_nueva)

# Ejercicio 6
# Desarrollar un programa que determine si ese entero es un número primo. En caso de no
# ser primo debe informar la cantidad de divisores y la suma de los mismos.
# Por ejemplo, si se ingresa:
# 881 debe informar: El número 881 es primo
# 15 debe informar: El número 15 no es primo ya que tiene 4 divisores y la suma de
# ellos es 24

numero = int(input("Ingrese un número: "))
suma = 0
contador = 0

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        suma += divisor
        contador += 1

if contador == 2:
    print("El número", numero, "es primo")
else:
    print(
        "El número",
        numero,
        "no es primo ya que tiene",
        contador,
        "divisores y la suma de ellos es",
        suma,
    )
