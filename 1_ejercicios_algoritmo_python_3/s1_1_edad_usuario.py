"""Cree un programa que lea la edad de un usuario y muestre cuántos años tendrá el usuario dentro
de tantos años como este indique. Por ejemplo, si el usuario tiene 20 años y quiere saber cuántos años tendrá
dentro de 15 años, el programa deberá mostrar que tendrá 35 años"""

# Algoritmo años proximos

#     entero edad_actual,edad_anios,edad_futura
#     imprimir("Cual es tu edad:")
#     leer(edad_usuario)
#     imprimir("Cuantos años tendra en: ")
#     leer (edad_anios)

#     edad_futura= edad_actual + edad_anios
#     imprimir(edad_futura)

# FinAlgoritmo


edad_actual = int(input("Cual es tu edad: "))
edad_anios = int(input("Cuantos años tendra en: "))
edad_futura = edad_actual + edad_anios
print("Tu edad futura es: ", edad_futura, "años")

