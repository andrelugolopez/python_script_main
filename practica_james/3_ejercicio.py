#3 > Cree un programa que usando el ciclo while le pregunte al usuario si desea salir del programa 
# (Use el ciclo while para pedirle al usuario que detenga el programa)


while True:
    respuesta = input("Desea salir del programa: ")
    if respuesta == "salir":
        print("Usted salio del programa")
        break
    else:
        print(respuesta)

