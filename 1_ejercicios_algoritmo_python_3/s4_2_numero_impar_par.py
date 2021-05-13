#2. Cree un programa que lea un número y muestre si este es par o impar. Use funciones. Haga pruebas de escritorio. 
#Pseudocodigo
#Real numero
#Proceso
#numero % 2 es igual a 0
#imprimir
#Numero par
#Sino imprimir número impar


def revisar_par_impar(numero):
    if numero % 2 == 0:
        print("Es un número par")
    else:
        print("Es un número impar")
        return numero

numero = float(input("Ingrese número: "))
resultado = revisar_par_impar(numero)
