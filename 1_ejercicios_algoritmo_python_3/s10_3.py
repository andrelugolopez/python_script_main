# programa que solicite al usuario nombre de un continente
# mostrar paises del continente seleccionadom por el usuario
# diccionario
# ciclo for 

def ingresar_continente():
    return str(input("Ingrese un continente: ")).lower()

def diccionario_continente():
    return {"america":["colombia","argentina","brasil"],
            "europa":["portugal","suiza","italia"],
            "asia":["rusia","corea del sur","china"],
            "africa":["egipto","nigeria","kenia"],
            "oceania":["nueva zelanda","australia","palaos"]}

def obtener_paises(dato_ingresado,continentes):
    if dato_ingresado in continentes:
        return continentes[dato_ingresado]

    else:
        print("-_"*20)
        print("¡Al parecer te falta cultura general!")
        print("--- Por favor intente de nuevo ---")
        print(" Te falta dinero para conocer mas")
        exit()

def imprimir_paises(paises):
    for pais in paises:
        print(f"{pais}")

#--------------------------------------------------------------------

# llamar funciones

dato_ingresado = ingresar_continente()
continentes = diccionario_continente()
paises = obtener_paises(dato_ingresado,continentes)
print("·"*40)
imprimir_paises(paises)
