#6. Cree un programa que calcule el promedio de 10 números.
# Use ciclo while. Use funciones. Haga pruebas de escritorio.
#  
def calcular_promedio_numeros():
    x = 0
    lista = []
    while x < 10:
        numeros_usuario = float(input("Cual número quiere incluir para el promedio: "))
        x = x + 1
        lista.append(numeros_usuario)
    promedio = sum(lista)/float(len(lista))
    return promedio

promedio = calcular_promedio_numeros()
print(f"Su promedio es: {promedio}")
