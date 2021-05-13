#Problema
#iterar los elementos del array usando while
#Crear otro arreglo identico, pero con todos los elementos incrementados en 1. Usar ciclo for y atraves de la iteración formar el nuevo arreglo con sus elementos como se piden
#Calcular el promedio de los elementos del arreglo. Usar for.

#Datos:
#lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] esto es una lista anidada

#Solucion
#Iterar elementos del array con while
def iterar_lista():
    #index hace el papel de indice dentro de while porque empieza en 0 y termina en la longitud de la lista menos 1
    #al hacer print sale 0 3, 1 3 y 2 3 porque me muestra el contador de la lista y el tamaño de las listas. EL tamaño de la lista en esl numero 3.
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Índice de lista
    longitud_matriz = len(matriz)
    index = 0
    # Recorro la matriz por cada lista
    while index < longitud_matriz:
        lista = matriz[index] # La lista actual

        # Índice de elementos
        sub_index = 0
        longitud_lista = len(lista)
        # Recorro la lista por cada elemento
        while sub_index < longitud_lista: # Recorro los elementos de la lista interna
            print(lista[sub_index]) 
            sub_index += 1
        index +=1

# Iterar por todos los elementos del arreglo utilizando el ciclo “for” y mostrarlos en pantalla.

# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# 
# # Por cada elemento en matriz
# for lista in matriz:
#     for elemento in lista:
#         print(elemento)

#Crear otro arreglo identico, pero con todos los elementos incrementados en 1. Usar ciclo for y atraves de la iteración formar el nuevo arreglo con sus elementos como se piden


# Arreglo idéntico con los elementos incrementados en 1
# Usar ciclo for
# Formar el nuevo arreglo con el for

# Defino la matriz con 3 listas
#matriz = [
#    [1, 2, 3], # << Lista
#    [4, 5, 6],
#    [7, 8, 9]
#]
#
## Defino una lista nueva para almacenar los valores nuevos
#matriz_nueva = []
#
## Recorro cada lista que se encuentra en la matriz
#for lista in matriz:
#    # Creo una lista nueva para los valores individuales
#    lista_nueva = []
#    # Recorro los elementos de la lista actual que saqué de matriz
#    for elemento in lista:
#        # En la lista nueva, agrego el elemento incrementado en 1
#        lista_nueva.append(elemento+1)
#    
#    # Agrego esa lista que cree a la matriz nueva
#    matriz_nueva.append(lista_nueva)
#
#print()
#print("-- Matriz Original --")
#print(matriz)
#print("-- Matriz Nueva --")
#print(matriz_nueva)

#Calcular el promedio de los elementos del arreglo. Usar for.

# Promedio = la suma de todos los elementos
# Dividido la cantidad de elementos

matriz = [
    [1, 2, 3], # 6
    [4, 5, 6], # 15
    [7, 8, 9], # 24
]

suma = 0
contador = 0
for lista in matriz:
    contador += len(lista)
    suma += sum(lista)

print("El promedio es")
print(suma/contador)

#iterar_lista()
