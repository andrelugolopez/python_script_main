#6. En una empresa se requiere un sistema de información que registre sus nuevos usuarios.
#Cada vez que un usuario se registra debe introducir los siguientes datos:
#documento, nombres, apellidos, edad, peso, estatura.
#Cree un sistema de información que reciba los datos de registro de cada cliente por teclado,
#luego de realizado el registro el sistema debe mostrar al usuario el mensaje "Registro exitoso".
#Si el usuario desea consultar su registro debe poder hacerlo a través de su documento. 


print("sistema de información")

informacion = {
            "documento": None,
            "nombres": None,
            "apellidos": None,
            "edad": None,
            "peso": None,
            "estatura": None,
             }

listado_usuarios = []


preguntar = True
while preguntar: 
    print("Por favor seleccione una de las siguientes opciones de acuerdo a lo que quiere realizar digitando el numero que corresponde: ")
    print("1: Registrar usuario \n2: Buscar usuario \n3: Salir")
    opcion = input("Ingrese la opcion: ")
    if opcion == "1":
        informacion["documento"] = input("Ingrese su documento: ")
        informacion["nombres"] = input("Ingrese sus nombres: ")
        informacion["apellidos"] = input("Ingrese sus apellidos: ")
        informacion["edad"] = input("Ingrese su edad: ")
        informacion["peso"]= input("Ingrese su peso: ")
        informacion["estatura"]= input("Ingrese su estatura: ")
        listado_usuarios.append(informacion)
        print("Registro exitoso")
    elif opcion == "2":
        documento_buscar = input("Ingrese número de documento que desea buscar: ")
        for diccionario in listado_usuarios:
            if documento_buscar == diccionario.get("documento"):
                print(f"Sus datos son: \n{diccionario}")
    elif opcion == "3":
        preguntar = False
        print("Usted ha salido del programa")
    else:
        print("Usted ingreso una opción no valida")
    





    

