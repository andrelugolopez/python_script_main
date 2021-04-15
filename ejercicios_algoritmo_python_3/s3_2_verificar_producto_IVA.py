#2. En un supermercado se tiene los siguientes productos: lentejas, crema, arroz y vino.
#Las lentejas y el arroz no pagan IVA, el vino y la crema si.
#Cree un programa que reciba el nombre de alguno de los productos mencionados y muestre si el producto paga IVA o no.
#Use funciones. Haga pruebas de escritorio.

#Problema:
#lentejas,arroz = no paga IVA
#vino,crema = si paga IVA

#datos:
#productos
#producto, IVA
#solucion:

def consultar_iva(producto):
    if producto == "lentejas" or producto == "arroz":
        print("No paga IVA")
    elif producto == "vino" or producto == "crema":
        print("Paga IVA")
    else:
        print("ERROR: El producto no existe")

entrada_producto = input("ingrese un producto: ").lower()
consultar_iva(entrada_producto)
