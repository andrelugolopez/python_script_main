#1. Dado la siguiente lista: 
#lista = [1,2,3,4,5,6,7,8,9,10]; 

print("-------------------------------------------")
#a) Usando ciclo for recorra la lista imprimiendo cada uno de sus elementos.
print("Lista con ciclo for: ")
lista = [1,2,3,4,5,6,7,8,9,10]

for elemento in lista:
    print(elemento)

print("-------------------------------------------")
#b) Usando ciclo while recorra la lista imprimiendo cada uno de sus elementos. 
print("Lista con ciclo while: ")

longitud_lista = len(lista)
elemento = 0
while elemento < longitud_lista:
    print(lista [elemento])
    elemento += 1
print("-------------------------------------------")
#c) Usando ciclo for recorra la lista imprimiendo cada uno de sus elementos aumentados en 3
print("Lista con ciclo for con aumento en 3: ")

for indice in range (longitud_lista):
    numero = lista[indice]
    numero +=3
    lista[indice] = numero
print(f"lista con incremento {lista}")

print("-------------------------------------------")
# d)Usando ciclo while recorra la lista imprimiendo cada uno de sus elementos aumentados en 3.

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"lista original: {lista}")

indice = 0
while indice < longitud_lista:
    elemento = lista[indice]       
    elemento += 3
    lista[indice] = elemento
    indice += 1
print(f"lista con incremento en 3: {lista}")

print("-------------------------------------------")
# e)Usando ciclo for recorra la lista imprimiendo únicamente los números impares.
lista = [1,2,3,4,5,6,7,8,9,10]
print("Números impares con ciclo for: ")

for indice in range (longitud_lista):
    elemento = lista[indice]
    if elemento % 2 == 1:
        lista[indice] = elemento
        print(f"{elemento}")
print("-------------------------------------------")
# f)Usando ciclo while recorra la lista imprimiendo únicamente los números pares. 
lista = [1,2,3,4,5,6,7,8,9,10]
print("Números pares con ciclo while: ")

def mostrar_numeros_pares(lista):
    indice = 0
    while indice < longitud_lista: 
        elemento = lista[indice]
        if elemento % 2 == 0: 
            lista[indice] = elemento  
            print(f"{elemento}")        
        indice += 1        

mostrar_numeros_pares(lista)

print("-------------------------------------------")
