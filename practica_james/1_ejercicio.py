#1) Cree un programa que agregue 10 elementos a una lista, y luego la imprima

lista = []

def agregar_a_la_lista(lista):
    for i in range (10):
        elementos = input("Ingrese 10 elementos: ")   
        lista.append(elementos)
    return lista

resultado =  agregar_a_la_lista(lista)
print(resultado)

