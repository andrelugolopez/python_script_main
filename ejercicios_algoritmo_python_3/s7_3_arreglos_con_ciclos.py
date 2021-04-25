#3. Dado el arreglo [1,2,3,4,5,6] 
#● Iterar por todos los elementos dentro del arreglo utilizando while y mostrarlos en pantalla
# ● Iterar por todos los elementos dentro del arreglo utilizando el ciclo “for” y mostrarlos en pantalla. 
#● Mostrar todos los elementos dentro del arreglo sumándole uno a cada uno. 
#● Crear una copia del arreglo usando el ciclo “for” pero con todos los elementos incrementados en 1
# ● Calcular el promedio de todos los elementos del arreglo 


lista = [1,2,3,4,5,6]

longitud_lista = len(lista)

print("Iteración con ciclo while:")

i = 0
while i < longitud_lista:
    print(lista[i])
    i+= 1
    
print("-------------------------------------------------")

print("Iteración con ciclo for:")

for x in lista:
    print(x)
        
print("-------------------------------------------------")

print("Arreglo sumandole sumandole uno a cada uno:")

i = 0
while i < longitud_lista:
    valor_lista = lista[i]       
    valor_lista += 1
    lista[i] = valor_lista
    i += 1
print(lista)

print("-------------------------------------------------")

print("Copia del arreglo con aumento en uno con cliclo for")

lista = [1,2,3,4,5,6]
lista_for = lista.copy()
longitud_lista = len(lista_for)

print(f"Copia de la lista: {lista_for}")


for indice in range (0,longitud_lista):
    numero = lista_for[indice]
    numero += 1
    lista_for[indice] = numero

print(f"lista con incremento {lista_for}")

print("-------------------------------------------------")

lista = [1,2,3,4,5,6]

print("Promedio de la lista")

def calcular_promedio_lista(lista):
    promedio = sum(lista)/len(lista)
    return promedio

resultado = calcular_promedio_lista(lista)
print(f"El promedio de la lista es: {resultado}")

print("-------------------------------------------------")
