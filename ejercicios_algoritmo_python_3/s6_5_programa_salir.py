#5. Cree un programa que pregunte al usuario si desea salir, si o no “S/N”, si el usuario teclea la letra S el programa se detendrá, de lo contrario continuará ejecutándose.
#Use ciclo while. Use funciones. Haga pruebas de escritorio. 

def salir_del_sistema():
    respuesta_usuario = "N"
    while respuesta_usuario != "s":
        respuesta_usuario = input("Introduzca \"S\" para salir del programa o \"N\" para no salir del programa: ").lower()
        if "s" == respuesta_usuario:
            print("Salió del sistema")
            exit()         

salir_del_sistema()

