# programa que implemente una funcion
# esta reciba como argumento un arreglo
# retorne la suma de los cuadrados de sus elementos
# imprimir resultado 

def cuantos_elementos():
    try:
        elemento = int(input("¿Cuantos elementos desea? : "))
    except:
        print("¡Por favor ingrese un numero entero!")
        exit()
    return elemento
    
def guardar_arreglo(elementos):
    arreglo = []
    for _ in range(elementos):
        try:
            numero = int(input("Ingrese un dato: "))
        except:
            continue
        arreglo.append(numero)
    return arreglo

def suma_cuadrados(lista):
    # 
    suma = 0
    for numero in lista:
        elemento = numero**2
        print(elemento)
        suma += elemento
    return suma

#--------------------------------------------------------------------------------------

# llamar funciones
print("")
elementos = cuantos_elementos()
print(f"{elementos}")
print("·"*40)
lista = guardar_arreglo(elementos)
print("-"*40)
print(">>> Arreglo <<<")
print(f"{lista}")
resultado_suma = suma_cuadrados(lista)
print("-"*40)
print(f"{resultado_suma}")
