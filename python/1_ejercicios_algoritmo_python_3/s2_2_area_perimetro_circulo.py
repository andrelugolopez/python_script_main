"""Cree un programa que tome el radio de un círculo e imprima su área y perímetro. Use funciones. Haga
pruebas de escritorio"""

#pseudocodigo
#VARIABLES
#Real radio_ciculo, area_circulo, perimetro_circulo
#CONTANTE
#VALOR_PI
#PROCESO
#area_circulo = VALOR_PI * radio_circulo **2
#area_perimetro= 2 * VALOR_PI * radio_circulo

radio_circulo = float(input("Cual es el radio del circulo: "))
VALOR_PI = 3.141592
if radio_circulo < 0:
    print("ERROR: El radio no debe ser negativo")
    exit()


def calcular_area_circulo (radio_circulo):
    area_circulo = VALOR_PI * (radio_circulo ** 2)
    return area_circulo
    
def calcular_perimetro_circulo (radio_circulo):
    perimetro_circulo = 2 * VALOR_PI * radio_circulo
    return perimetro_circulo

area_circulo = calcular_area_circulo(radio_circulo)
perimetro_circulo = calcular_perimetro_circulo(radio_circulo)

print("El area del circulo es: ", round(area_circulo,2))
print("El perimetro del circulo es: ", round(perimetro_circulo,2))


