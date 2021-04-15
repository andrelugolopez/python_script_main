#Cree un programa que lea la edad de un usuario e imprima un mensaje que diga si el usuario es mayor de edad o no.
# Use funciones. Haga pruebas de escritorio.

#Pseudocodigo
#Entero entrada_edad
#Proceso
#Si entrada_edad mayo o igual a 18
#Imprimir
#"Es mayor de edad"
#Sino "Es menor de edad"


def evaluar_edad_usuario(edad):
    if edad >= 18:
        print("Es mayor de edad")
    else: 
        print("Es menor de edad")    

entrada_edad = int(input("Ingrese su edad: "))
if entrada_edad < 0:
    print("ERROR la edad no puede ser negativa")
    exit()

evaluar_edad_usuario(entrada_edad)
