#4. Cree un programa que muestre los números impares entre 1 y n. Use ciclo while.
#  Use funciones. Haga pruebas de escritorio. 


def mostrar_numeros_impares(limite):
    x = 1
    lista = []
    while x <= limite: 
        if x % 2 == 1: 
            lista.append(x)           
        x = x + 1
    print(lista)
limite = int(input("Indique el numero final para revisar los numeros impares: "))
mostrar_numeros_impares(limite)

