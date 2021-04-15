"""3. Cree un programa que tome el lado de un cubo e imprima su volumen. Use funciones, incluya un parámetro
con valor por defecto. Haga pruebas de escritorio."""
#PSEUDOCODIGO
#Variables
#volumen
#lado
#PROCESO
#volumen = lado **3
#volumen = lado*lado**lado
#iMPRIMIR RESULTADO


#SOLUCIÓN

def calcular_volumen_cubo (lado_cubo):
    volumen = lado_cubo**3
    return volumen   
lado = float(input("Cuanto mide el lado: "))
if lado < 0:
    print(f"ERROR: No se puede operar con el lado negativo > {lado}")
    exit()

#RESULTADO
resultado = calcular_volumen_cubo(lado)
print("El volumen del cubo es:", resultado)
