#1. Cree un programa que lea los tres ángulos internos de un triángulo y
#  muestre si los ángulos corresponden a un triángulo o no. Use funciones. Haga pruebas de escritorio. 
#Pseudocodigo
#Variables
# Real angulo_uno, angulo_dos, angulo_tres
#Proceso
#suma_angulos = angulo_uno + angulo_dos + angulo_tres
#Si suma_angulos == 180
#Imprimir
#Si es un triangulo
#Si no no es un triangulo

def calcular_triangulo(angulo_uno, angulo_dos, angulo_tres):
    triangulo = angulo_uno + angulo_dos + angulo_tres
    if triangulo == 180:
        print ("Es un triangulo")
    else:
        print("No es un triangulo")

angulo_uno = float(input("¿Cuál es el ángulo uno del triangulo? "))
if angulo_uno < 0:
    print("ERROR  el numero no puede ser negativo")
    exit()
angulo_dos = float(input("¿Cuál es el ángulo dos del triangulo? "))
if angulo_dos < 0:
    print("ERROR  el numero no puede ser negativo")
    exit()
angulo_tres = float(input("¿Cuál es el ángulo tres del triangulo? "))
if angulo_tres < 0:
    print("ERROR el numero no puede ser negativo")
    exit()

calcular_triangulo(angulo_uno, angulo_dos, angulo_tres)
