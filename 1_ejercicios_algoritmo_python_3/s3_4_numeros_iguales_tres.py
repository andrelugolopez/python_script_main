# Cree un programa que reciba tres números y muestre el mayor.
# En caso de que los números sean iguales también
# se debe mostrar al usuario. Use funciones. Haga pruebas de escritorio

# PROBLEMA #
# DATOS #
# numero1
# numero2
# numero3

def pedir_numero(n):
    try:
        return float(input(f"Ingrese el número {n}: "))
    except:
        print("ERROR: No se ha podido completar la operación")
        exit()
    return None

#Pido los datos por teclado
numero1 = pedir_numero(1)
numero2 = pedir_numero(2)
numero3 = pedir_numero(3)

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)

if numero1 == numero2 == numero3:
    print("Todos son iguales")
else:
    print(f"El número mayor es: ({round(numeros[0])})")
