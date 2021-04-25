# Cree un programa que cumpla con los siguientes requerimientos: En una clínica, se requiere un programa
# donde el usuario pueda consultar el día de su cita mediante su documento. La cita debe tener día y fecha. Si el
# usuario consulta, el programa debe mostrarle sus nombres, seguidos del día y hora de su cita. Una vez hecha la
# consulta, el programa le debe mostrar al usuario un mensaje preguntándole si desea cambiar el día ó fecha de su
# cita, de ser así el programa debe realizar tal cambio y mostrarle al usuario que el cambio solicitado ha sido
# exitoso. Use diccionarios.

# Requerimientos
# El usuario puede consultar el día de su cita mediante su documento
# La cita debe tener día y fecha
# Si el usuario consulta, debe mostrar
# > Nombres
# > Cita > Fecha
# Una vez hecha la consulta, el programa deberá preguntarle el usuario
# Si desea cambiar el día o la fecha
# #El programa debe realizar el cambio y mostrar el cambio por consola

### Diccionarios de datos ###
datos_usuario = {} # Llave = Documento :: Valor = Nombre
citas_usuario = {} # Llave = Documento :: Valor = Tuplas -> (Dia Mes Año)

### Ciclo de la aplicación ###
print("Bienvenido a la clínica Novameraki\n")

while True: # Ciclo infinito
    
    # Muestro las opciones que tiene disponible el usuario
    print("-"*50)
    print("¿Qué operación desea realizar?\n")
    print("1: Registrar nuevo usuario")
    print("2: Consultar citas")
    print("3: Registrar una nueva cita")
    print("4: Salir de la aplicación")
    print("-"*50)

    # Pido al usuario la opción
    opcion = int(input("Ingrese la opción que desea: "))
    
    print()
    
    # Si la opción no está entre 1 y 4
    if opcion < 1 or opcion > 4:
        # Imprimo un mensaje de salida
        print("Ha ingresado una opción incorrecta, recuerde ingresar una opción de 1 a 4")
    else:
        # La opción es correcta
        
        if opcion == 1:
            # Registrar un nuevo usuario
            
            # Pido el nombre de usuario para su registro
            nombre_usuario = input("Ingrese el nombre del usuario a registrar: ")
            
            # Pido el número de documento del usuario
            documento_usuario = input("Ingrese el documento del usuario a registrar: ")

            # Compruebo que el número de documento no haya sido registrado previamente
            if documento_usuario in datos_usuario:
                print(f"El documento {documento_usuario} ya ha sido registrado previamente en nuestra base de datos...")
            else:
                # El número de documento no está registrado

                # Registro el número de documento como llave y su nombre como nombre de usuario
                datos_usuario[documento_usuario] = nombre_usuario
                # De esta forma, si le entrego a datos usuario el documento del usuario
                # El me va a regresar el nombre del usuario

                print(f"\nSe ha registrado el usuario {nombre_usuario} con el número de documento '{documento_usuario}'")

        elif opcion == 2:
            # Consultar una cita
            
            # Pido el número de documento al usuario
            documento_usuario = input("Por favor ingrese su número de documento: ")
            
            # Compruebo que el número de documento exista
            if documento_usuario in datos_usuario:

                # Obtengo el nombre de usuario con base en el documento
                nombre_usuario = datos_usuario[documento_usuario]

                # Compruebo que el usuario tenga citas registradas en el diccionario
                if documento_usuario in citas_usuario:

                    # Obtengo la cita que tiene el usuario
                    cita_usuario = citas_usuario[documento_usuario]

                    # Creo variables para obtener el día, mes y año
                    dia = cita_usuario[0]
                    mes = cita_usuario[1]
                    anyo = cita_usuario[2]

                    # Muestro la cita que tiene el usuario
                    print(f"El usuario {nombre_usuario} tiene una cita registrada el {dia} del mes {mes} del año {anyo}")
                    
                    # Pregunto al usuario si desea cambiar la fecha de la cita
                    decision_usuario = input("\n¿Deseas cambiar la fecha de la cita? (y/N): ").lower()
                    
                    # Si la decisión del usuario es afirmativa o positiva
                    if decision_usuario == "y":
                        
                        # Procedo a cambiar la fecha de la cita

                        # Pido el día de la cita
                        dia = int(input("Ingrese el día de la nueva cita: "))
                        
                        # Si el día no está entre los límites
                        if dia < 0 or dia > 32:
                            print("Ha ingresado un valor incorrecto para día, por favor ingrese un valor entre 1 y 32")
                            continue
                        
                        # Pido el mes de la cita
                        mes = int(input("Ingrese el mes de la nueva cita: "))

                        # Si el mes no está entre los límites
                        if mes < 0 or mes > 12:
                            print("Ha ingresado un valor incorrecto para mes, por favor ingrese un valor entre 1 y 12")
                            continue
                        
                        # Pido el año de la cita
                        anyo = int(input("Ingrese el año de la nueva cita: "))
                        
                        # Si el año no está entre los límites
                        if anyo < 1900:
                            print("Ha ingresado un valor incorrecto para año, por favor ingrese un valor menor a 1900")
                            continue

                        # Creo el objeto de tupla para la cita
                        nueva_cita_tupla = (dia, mes, anyo)
                        
                        # Accedo con la llave al diccionario de citas para modificar su valor
                        # De esta manera modifico la cita registrada por el usuario
                        citas_usuario[documento_usuario] = nueva_cita_tupla

                        # Creo variables para obtener el día, mes y año
                        dia = nueva_cita_tupla[0]
                        mes = nueva_cita_tupla[1]
                        anyo = nueva_cita_tupla[2]

                        # Muestro la cita que tiene el usuario
                        print(f"\nSe ha modificado satisfactoriamente la cita para el usuario {nombre_usuario}. La nueva fecha de su cita es el {dia} del mes {mes} del año {anyo}")

                else:
                    # El usuario no tiene citas registradas
                    print(f"No hay citas registradas para el usuario {nombre_usuario}")
            else:
                # No existe el documento en el diccionario de datos
                print(f"\nEl documento '{documento_usuario}' no se encuentra registrado en nuestra base de datos...")

        elif opcion == 3:
            # Registrar una nueva cita
            
            # Obtengo el número de documento del usuario
            documento_usuario = input("Por favor ingrese su número de documento: ")

            # Compruebo que el documento del usuario esté registrado en la base de datos
            if documento_usuario in datos_usuario:

                # Obtengo el nombre de usuario
                nombre_usuario = datos_usuario[documento_usuario]

                # Doy un saludo de bienvenida
                print(f"\nBienvenido {nombre_usuario} a nuestro portal de citas de la clínica Novameraki")
                
                # Doy un mensaje de notificación cuando la cita ya esté registrada para el usuario
                if documento_usuario in citas_usuario:
                    cita = citas_usuario[documento_usuario]
                    print(f"Se ha detectado una cita previamente registrada... esta operación sobrescribirá la cita actual: {cita[0]}/{cita[1]}/{cita[2]}")
                    
                    # Pregunto al usuario si desea continuar
                    decision_usuario = input("\n¿Desea continuar? (y/N): ").lower()

                    # Si el usuario toma la decisión de no continuar
                    if decision_usuario != "y":

                        # Continue reinicia el ciclo
                        continue

                # Pido el día de la cita
                dia = int(input("Ingrese el día de la cita: "))
                
                # Si el día no está entre los límites
                if dia < 0 or dia > 32:
                    print("Ha ingresado un valor incorrecto para día, por favor ingrese un valor entre 1 y 32")
                    continue
                
                # Pido el mes de la cita
                mes = int(input("Ingrese el mes de la cita: "))

                # Si el mes no está entre los límites
                if mes < 0 or mes > 12:
                    print("Ha ingresado un valor incorrecto para mes, por favor ingrese un valor entre 1 y 12")
                    continue
                
                # Pido el año de la cita
                anyo = int(input("Ingrese el año de la cita: "))
                
                # Si el año no está entre los límites
                if anyo < 1900:
                    print("Ha ingresado un valor incorrecto para año, por favor ingrese un valor menor a 1900")
                    continue

                # Creo el objeto de tupla para la cita
                cita_tupla = (dia, mes, anyo)

                # Registro la cita al usuario
                citas_usuario[documento_usuario] = cita_tupla

                print("\nSu cita se ha registrado con éxito")

            else:
                # El usuario no está registrado
                print(f"\nEl documento '{documento_usuario}' no se encuentra registrado en nuestra base de datos...")

        elif opcion == 4:
            # Salir de la aplicación
            break # Porque el ciclo es infinito, uso un break para romperlo

print("Gracias por usar nuestros servicios.")
