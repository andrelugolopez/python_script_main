#. Cree un programa que pida al usuario el nombre de un producto existente en una tienda, luego, que le muestre
#el precio del producto. El usuario debe poder elegir de entre por lo menos cinco productos. Use diccionarios.

#Problema
#Devolver precio del producto ingresado

diccionario_productos = {"canela": 2_000, "ciruelas": 4_000, "cerezas": 5_000, "mostaza": 7_000, "vino": 10_000} #Primero llave, luego valor
#print (diccionario_productos["Canela"])

producto_ingresado = input("Ingrese el nombre del producto: ").lower()

if producto_ingresado in diccionario_productos: #Con esto decimos: si el producto ingresado se encuentra dentro del diccionario (keys).
        print(diccionario_productos[producto_ingresado])
else: 
        print("El producto no se encuentra disponible en la tienda.")



#if producto_ingresado == diccionario_productos["Canela"]:
        #print("El precio de la canela es: ", diccionario_productos["Canela"])
#elif producto_ingresado == diccionario_productos["Ciruelas"]:
        #print("El precio de las ciruelas es: ", diccionario_productos["Ciruelas"])
#elif producto_ingresado == diccionario_productos["Cerezas"]:
        #print("El precio de las cerezas es: ", diccionario_productos["Cerezas"])
#elif producto_ingresado == diccionario_productos["Mostaza"]:
        #print("El precio de la mostaza es: ", diccionario_productos["Mostaza"])
#elif producto_ingresado == diccionario_productos["Vino"]:
        #print("El precio de los duraznos es: ", diccionario_productos["Vino"])


