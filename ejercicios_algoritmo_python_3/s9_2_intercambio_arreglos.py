#Dado los siguientes arreglos 
#arreglo1 = [[“A”, “B”, “C”], [“D”, “E”, “F”], [“G”, “H”, “I”]] 
#arreglo2 = [[“J”, “K”, “L”],[“M”, “N”, “O”], [“P”, “Q”, “R”]],
# use ciclos para intercambiar los elementos de los arreglos.

#print("---Arreglos originales---")
arreglo1 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
arreglo2 = [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]]

print("Original arreglo1: ", arreglo1)
print("Original arreglo2: ", arreglo2)
print("Intercambio: ")

copia_arreglo1 = arreglo1.copy()
for index in range(3):
    arreglo1[index] = arreglo2[index]
    arreglo2[index] = copia_arreglo1[index]

print("Intercambio arreglo1: ", arreglo1)
print("Intercambio arreglo2: ", arreglo2)

#SOLUCIÓN CON SWAP
#print("Intercambio arreglo1: ", arreglo1)
#print("Intercambio arreglo2: ", arreglo2)
#print("Intercambio: ")

#copia_arreglo1 = arreglo1.copy() 
#con .copy hago una copia independiente del arreglo. Sin .copy es una copia de referencia. copia_arreglo1 guarda los valores originales
#arreglo1[0], arreglo1[1], arreglo1[2] = arreglo2[0], arreglo2[1], arreglo2[2]
#arreglo2[0], arreglo2[1], arreglo2[2] = copia_arreglo1 [0], copia_arreglo1[1], copia_arreglo1[2]

#print("Intercambio arreglo1: ", arreglo1)
#print("Intercambio arreglo2: ", arreglo2)

#swap en listas
#>>> L=[1,2,3]
 #>>> print L
#[1,2,3]
 #>>> L[0],L[1] = L[1],L[0]
 #>>> print L
#[2,1,3]