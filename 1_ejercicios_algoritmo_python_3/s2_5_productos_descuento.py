# Cree un programa que tome el valor de un producto e imprima su precio final
#  si este tiene siempre un descuento del 10%. Use funciones. Haga pruebas de escritorio.

# Problema
# Precio final = valor_producto - 10% descuento

# Datos
# valor_producto
# descuento_10%
# precio_final

# Solucion del problema

#def main():
def calcular_precio_final(valor_producto, descuento):
    precio_final = round(valor_producto - descuento,2)
    return precio_final

# Defino mis variables
descuento = 10
valor_producto = float(input("Ingrese valor del producto: $"))
if valor_producto < 0:
    print("No se admite valor producto negativo")
    exit ()

# Calculo el precio final
descuento_precio = valor_producto * descuento / 100
precio_final = calcular_precio_final(valor_producto, descuento_precio)

# Imprimo los resultados
print(f"El descuento con {descuento}% de {valor_producto} es: $ {precio_final} ")

#if __name__ == "__main__":
    #main()
