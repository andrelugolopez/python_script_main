# Cree un programa que use una función de un parámetro,
# a la cual se le pase como argumento un arreglo, de
# tal manera que la función retorne la 
# longitud(número de elementos) del arreglo.

def generar_lista():
    numeros_entrada = input("Ingrese los valores que desea en la lista separados por comas (x,y,z,n): ")
    numeros = numeros_entrada.split(",")
    return numeros

def obtener_longitud_lista(lista):
    return len(lista)

print("Bienvenido al programa para imprimir el número de elementos de un arreglo")
lista = generar_lista()
print(f"La longitud de la lista {lista}:")
print(obtener_longitud_lista(lista))
