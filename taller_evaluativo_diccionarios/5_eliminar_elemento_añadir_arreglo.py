#5. Dado el siguiente arreglo [1, 2, 3, 4, 500, 420, -100]

print("---------------------------------------------------")
#elimine el elemento de índice 4 y a continuación
arreglo = [1, 2, 3, 4, 500, 420, -100]
print(f"Arreglo original: {arreglo}")
eliminar = arreglo.pop(4)
print(f"Eliminar elemento indice (4) 500: {arreglo}")

print("-----------------------------------")
#elimine el último elemento de la lista usando el método pop
#(si al método pop no se le pasa argumento, eliminará el último elemento de la lista)
#el cual puede consultar aquí: 
#https://www.geeksforgeeks.org/python-list-pop/ . Agregue el elemento 520 usando el método append.
eliminar_ultimo_elemento = arreglo.pop()
print(f"Eliminar último elemento: {arreglo}")

print("---------------------------------------------------")
#Finalmente, haga una copia "independiente del arreglo" usando el método copy
#el cual puede consultar acá: https://www.programiz.com/python-programming/methods/list/copy.
copia_arreglo = arreglo.copy()
print(f"Arreglo original: {arreglo}")
print(f"Copia de arreglo: {copia_arreglo}")

print("---------------------------------------------------")

