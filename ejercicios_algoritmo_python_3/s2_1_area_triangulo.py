"""Cree un programa que tome la base y la altura de un triángulo e imprima su área. Use funciones, incluya dos
parámetros con valor por defecto. Haga pruebas de escritorio"""
#Pseudocodigo
#Real base_triangulo, altura_triangulo, aerea_triangulo
#CONSTANTE
#NUMERO_DOS
#aerea_triangulo = base_triangulo * altura_triangulo / 2
#Imprime area triangulo


#Definir variables
base_triangulo = float(input("Cual es la base del triangulo: "))

if base_triangulo < 0:
    print("ERROR: La base no debe ser negativo")
    exit()

altura_triangulo = float(input("Cual es la altura del triangulo: "))
if altura_triangulo < 0:
    print("ERROR: La altura no debe ser negativo")
    exit()

#Función
def calcular_area_triangulo(base_triangulo = 20, altura_triangulo = 30):
    NUMERO_DOS = 2
    area_triangulo = (base_triangulo * altura_triangulo) / NUMERO_DOS
    return area_triangulo

area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
print("El area del triangulo es: ", area_triangulo)