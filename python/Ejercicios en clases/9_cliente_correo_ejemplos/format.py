nombre_producto1 = input("Ingrese producto")
precio_producto1 = input("Ingrese precio producto")
precio_final_producto1 = int(precio_producto1) * 0.19 + int(precio_producto1)
formato_producto1 = "<h1>Precio: {} Producto: {} precio con IVA: {} </h1>".format(precio_producto1, nombre_producto1, precio_final_producto1)
