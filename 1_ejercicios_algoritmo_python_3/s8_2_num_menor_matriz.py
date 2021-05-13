'''
 Funcion que permita encontrar el numero menor contenido en una matriz recibida como parametro
'''
#funcion para saber cuantas listas desea el usuario
def ingresar_listas():
    return int(input("Cuantas listas desea: "))

def ingresar_elementos():
    return int(input("¿Cuantos elementos quiere en cada lista? : "))
 
 #se declara la funcion que se creea las listas que el usuario deseo
def generar_matriz (cuantas_listas,elementos_lista):
    if cuantas_listas > 0:
        # se crea la matriz para alamacenar las listas dentro
        matriz = []
        # itera las veces que quiere las listas
        for i in range(cuantas_listas):
            print(f"{i+1}. lista")
            # en ( listas = [] )  se guarda los numeros que desee
            listas = []
            # itera los veces que quiere ingresar numeros 
            for i in range(elementos_lista):
                elemento = float(input("Ingrese un numero: "))
                    # se guarda los elementos recibidos en la lista
                listas.append(elemento)
                # se guardan las listas en la matriz
            matriz.append(listas)
        return matriz    
    else:
        print("    Ingreso un numero negativo")
        print(">>> Por favor intente de nuevo <<<")

# 
def numero_menor(matrices):
    # 
    matriz_nueva = []
    # 
    for lista in matrices:
        # 
        elementos_matriz = []
        # 
        for elemento in lista:
            # 
            elementos_matriz.append(elemento)
        #  
        elementos_matriz.sort()
        matriz_nueva.append(elementos_matriz)
    matriz_nueva.sort()
    print(f"{matriz_nueva}")
    return matriz_nueva[0][0]

#-------------------------------------------------------------------------

# llamar funciones 
print("·"*35)
cuantas_listas = ingresar_listas()
print("·"*35)
elementos_lista = ingresar_elementos()
print("-"*35)
matrices = generar_matriz(cuantas_listas,elementos_lista)
print("")
print(f"Esta seria su lista de listas: {matrices}")
print("-"*35)
menor = numero_menor(matrices)
print(">>> Numero menor de cada lista <<<")
print(f"{menor}")