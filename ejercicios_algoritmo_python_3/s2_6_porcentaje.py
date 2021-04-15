"""6. Cree un programa que lea una cantidad e imprima un porcentaje a calcular requerido sobre esa cantidad.
Use funciones. Haga pruebas de escritorio."""
#Pseudocodigo
#Entero cantidad, porcentaje
#CONSTANTE
#NUMERO_CIEN
#resultado_conversion_porcentaje = portencaje / NUMERO_CIEN
#resultado_porcentaje = cantidad * porcentaje
#Imprimir resulado

cantidad = float(input("Cual es la cantidad a sacar el porcentaje: "))

if cantidad < 0:
    print("ERROR: La cantidad no debe ser negativo")
    exit()

try: 
    porcentaje = float(input("Que porcentaje desea sacar (Escribir sin % solo número): "))

except: 
    print("Revisa que no halla ingresado el simbolo %")
    exit()

if porcentaje > 100:
    print("ERROR: El porcentaje no puede ser mayor a 100")
    exit()
elif porcentaje < 0:
    print("ERROR: El porcentaje no debe ser negativo")
    exit()

def convertir_porcentaje_entero(porcentaje):
    NUMERO_CIEN = 100
    resultado = porcentaje / NUMERO_CIEN
    return resultado

def calcular_cantidad_porcentaje(cantidad, porcentaje):
    resultado = cantidad * porcentaje
    return resultado

resultado_conversion_porcentaje = convertir_porcentaje_entero(porcentaje)
resultado_porcentaje = calcular_cantidad_porcentaje(cantidad, resultado_conversion_porcentaje)
print("El porcentaje de la cantidad es: ", resultado_porcentaje)
