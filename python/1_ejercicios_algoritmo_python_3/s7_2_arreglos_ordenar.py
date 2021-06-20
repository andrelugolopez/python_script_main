# progranma que implemente un arreglo de 10 elementos(dos gitos)
# ordenarlos de menor a mayor 
# imprimirlos como entran y ya ordenados 
# luego invertir el orden de los elemnetos del array 
# que el ultimo pase de primero y asi sucesivamente
# luego imprimir como quede

# 
def ingresar_elementos():
    lista = []
    for _ in range(10):
        try:
            elemento = float(input("Ingrese un numero: "))
        except:
            print("¡POR FAVOR! - ingrese un dato correcto")
            exit()
        lista.append(elemento)
    return lista

# la funcion (.sort()) organiza los numeros de menor a mayor
def ordenar_ascendente(lista):
    lista.sort()
    return lista

# la funcion (.reverse()) organiza la lista de forma alrevez 
def ordenar_descendente(lista):
    lista.reverse()
    return lista


# llamar funciones

print("-"*35)
lista = ingresar_elementos()
print("    Numeros que ingreso")
print("·"*35)
print(f"{lista}")
print("-"*35)
ascendente = ordenar_ascendente(lista)
print(">>> Numeros en orden <<<")
print("      Menor a Mayor")
print("·"*35)
print(f"{ascendente}")
print("-"*35)
descendente = ordenar_descendente(lista)
print(">>> Numeros invertidos <<<")
print("      Menor a Mayor")
print("·"*35)
print(f"{descendente}")

