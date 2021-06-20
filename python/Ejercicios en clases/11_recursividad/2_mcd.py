# Dos variables: 
# 1: 412 >> numero1 
# 2: 184 >> numero2

# Restar el más pequeño del más grande
# Condicional
# Si el numero1 es mayor al numero2:
#   numero1 - numero2 (al mayor le quito el menor)
# Sino: En caso que el numero2 sea mayor al numero1
#   numero2 - numero1 

def mcd(numero1, numero2):
    # Si ambos numeros son iguales, retorno el numero
    if numero1 == numero2:
        return numero1 # Este es el final
    elif numero1 > numero2: # Si numero1 es mayor a numero2
        numero1 -= numero2
    else: # En caso contrario
        numero2 -= numero1
    
    # Vuelvo a calcular el maximo común divisor
    return mcd(numero1, numero2)

# Defino mis variables
numero1 = int(input("Ingrese el valor del número 1: "))
numero2 = int(input("Ingrese el valor del número 2: "))

print("\nEl MCD es: ")
print(f">>> {mcd(numero1, numero2)} <<<")