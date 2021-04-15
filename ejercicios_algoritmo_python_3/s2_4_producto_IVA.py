"""4. Cree un programa que tome el precio de un producto e imprima su precio final al consumidor con un IVA de
19%. Use funciones, incluya por lo menos un parámetro con valor por defecto. Haga pruebas de escritorio."""
#PSEUDOCODIGO

#VARIABLE
#Real precio, precio_final

#CONSTANTE
#IVA

#PROCESO
#precio_final = precio * IVA

#IMPRIMIR RESULTADO


#SOLUCIÓN

def calcular_precio_final (precio, IVA = 1.19):
    precio_final = round(precio * IVA, 2)
    return precio_final

precio = (float(input("Cual es el precio del producto: ")))
if precio < 0:
    print("ERROR: El precio no puede ser negativo")
    exit()

#iMPRIMIR RESULTADO
resultado = calcular_precio_final(precio)
print("El valor del producto con IVA es: ", resultado)












