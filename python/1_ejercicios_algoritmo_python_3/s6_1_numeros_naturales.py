#1. Cree un programa que muestre los números naturales de 1 a n.
#Use ciclo while. Use funciones. Haga pruebas de escritorio. 

def calcular_numeros_naturales(numero_usuario):
    x = 1
    while x <= numero_usuario:
        print(x)
        x = x + 1

numero_usuario = int(input("Ingrese hasta que numero desea llegar: "))

calcular_numeros_naturales(numero_usuario)