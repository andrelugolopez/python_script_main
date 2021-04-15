#3. Cree un programa que lea un número y muestre si este es divisible entre cinco o no.
#Use funciones. Haga pruebas de escritorio. 
#Pseudocodigo
#Real numero
#Proceso
#numero % 5 es igual a 0
#imprimir
#Si es divisible entre cinco
#Sino imprimir el número no es divisible entre cinco


def calcular_divisible_cinco(numero):
    if numero % 5 == 0:
        print("Este número es divisible entre cinco")
    else:
        print("Este número no es divisible entre cinco")
    return numero

numero = float(input("Ingrese número: "))
resultado = calcular_divisible_cinco(numero)