#. Cree un programa que dado un número entero n, calcule su factorial(n).
#  Use ciclo for. Use funciones. Haga pruebas de escritorio. 

valor_anterior = 0

def calcular_factorial(numero):
    for i in range (1, numero):
        numero = numero * i
    return numero

try: 
    numero = int(input("Número que desea sacar su factorial: "))
except: 
    print("No se permite numeros con decimales")
    exit()
if numero < 1:
    print("ERROR: No se permite el numero cero ni numeros negativos")
    exit()

factorial = calcular_factorial(numero)
print(f"El factorial de su número es: {factorial}")



 
