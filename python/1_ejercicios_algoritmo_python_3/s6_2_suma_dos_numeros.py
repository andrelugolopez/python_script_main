#2. Cree un programa que calcula la suma de los primeros n números naturales.
# Use ciclo while.
# Use funciones. Haga pruebas de escritorio. 

def sumar_numeros_naturales(numero):
    x = 0
    resultado_suma = 0
    while x < numero_final:
        valor_anterior = resultado_suma
        resultado_suma = resultado_suma + (x + 1)
        print(f" {valor_anterior} + {x + 1} = {resultado_suma}")
        x = x + 1
        
numero_final = int(input("Hasta que numero natural desea realizar la suma: "))
sumar_numeros_naturales(numero_final)