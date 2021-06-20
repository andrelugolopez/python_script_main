# Cree un programa que reciba dos números y muestre el mayor.
# En caso de que los números sean iguales también 
# se debe mostrar al usuario.
# Use funciones. Haga pruebas de escritorio.

# PROBLEMA #
# Mostrar el mayor >> numero1, numero2
# Si son iguales:
#   >> "los números son iguales"

# DATOS #
# numero1
# numero2

# SOLUCIÓN

def pedir_numero(n):
    try:
        return float(input(f"Ingrese por favor, el número {n}: "))
    except:
        print("ERROR: No se ha podido completar la operación")
        exit()
    return None

def es_mayor(a, b):
    return a > b

def es_igual(a, b):
    return a == b

# Esta función evalúa cual número es mayor o menor, o si son iguales
def evaluar_numeros(numero1, numero2):
    if es_igual(numero1, numero2):
        print("Ambos números son iguales")
    elif es_mayor(numero1, numero2):
        print(f"El número 1 ({numero1}) es mayor que el número 2 ({numero2})")
    else:
        print(f"El número 2 ({numero2}) es mayor que el número 1 ({numero1})")

numero1 = pedir_numero(1)
numero2 = pedir_numero(2)

evaluar_numeros(numero1, numero2)
