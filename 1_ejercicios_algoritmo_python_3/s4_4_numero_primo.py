#4. Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no. Use funciones. Haga pruebas de escritorio. 
#Pseudocodigo
#Variable
#Real numero
#Lista numeros_primos
#Proceso
#Si numero se encuentra en lista numeros_primos
#Imprimir 
#El número es primo
#Sino imprimir "El número no es primo"

numeros_primos = [2,3,5,7,11,13]

def verificar_rango_numero(numero):
    if numero < 1 or numero >= 15:
        print("ERROR: Número no valido (Se permite numeros entre 1 y 15)")
        exit()

def validar_numero_primo(numero):
    if numero in numeros_primos:
        print("El número es primo")
    else:
        print("El número no es número primo")

try: 
    numero = int(input("Ingrese número entre 1 y 15 para verificar si es número primo: "))
except: 
    print("ERROR: Revisa que el numero ingresado sea entero")
    exit()
verificar_rango_numero(numero)
validar_numero_primo(numero)





