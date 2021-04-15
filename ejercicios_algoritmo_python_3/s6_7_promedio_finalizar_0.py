#7. Cree un programa que muestre el promedio de n números, dejándose de solicitar números cuando se introduzca el cero.
#Use ciclo while. Use funciones. Haga pruebas de escritorio. 

def calcular_promedio_numeros():
    lista = []
    while True:
        numero = float(input("Ingrese número: "))
        if numero == 0:
            break
        elif numero >= 0:
            lista.append(numero)
    promedio = sum(lista)/float(len(lista))
    return promedio

promedio = calcular_promedio_numeros()
print(f"Su promedio es: {promedio}")