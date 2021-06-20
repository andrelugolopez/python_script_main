#un diccionario es una estructura de datos
#es una estructura no ordenada
#es una estructura cuyos elementos son pares clave-valor, los cuales
#van separados por ,
#LAS LLAVES DE UN DICCIONARIO SON enteros, cadenas, tuplas etc cualquier
#elemento inmutable
#LOS VALORES PUEDEN SER: listas, diccionarios, cadenas, enteros, objetos...

print("------definicion------------")
diccionario_dias = {0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves"}
print("------lectura con sintaxis []------------")
#como la llave existe, no arroja error
print("dia semana llave 2: ", diccionario_dias[2])
#como la llave no existe, arroja error
#print("dia semana llave 4: ", diccionario_dias[4])
print("------lectura con sintaxis .get()------------")
#como la llave existe, no arroja error
print("dia semana llave 2: ", diccionario_dias.get(2))
#como la llave no existe, no arroja error, en este caso devuelve None
print("dia semana llave 4: ", diccionario_dias.get(4))
print("------tratar el None de .get()------------")
#si la llave existe, imprime "El dia existe"
#de lo contrario imprime "El dia No existe"
if diccionario_dias.get(2):
    print("El dia existe")
else:
    print("El dia No existe")
print("------imprimir un diccionario completo------------")
print("diccionario: ", diccionario_dias)
print("------asignacion------------")
#asiganmos valores pasando la clave dentro de corchetes
#Y SU RESPECTIVO VALOR A LA DERECHA DEL OPERADOR DE ASIGNACION
diccionario_dias[4] = "Viernes"
diccionario_dias[5] = "Sabado"
diccionario_dias[6] = "Domingo"
print("diccionario actualizado: ", diccionario_dias)

print("------borrado------------")
personas = {"Paola": "Ruiz", "Pedro": "Gonzalez", "Maria": "Velez"}
print("diccionario personas antes de borrado: ", personas)
#borramos el par Pedro-Gonzalez
#SI LA LLAVE NO EXISTE DURANTE EL BORRADO NOS ARROJA UN ERROR CRITICO
personas.pop("Pedro")
print("diccionario personas despues de borrado: ", personas)
#cuando eliminamos una llave con .pop() obtenemos de vuelta el valor de la llave
#que acabamos de eliminar
#print("valor que devuelve .pop(): ", personas.pop("Pedro"))
print("------estructuras de datos como valores------------")
print("------listas como valores------------")
#ESTE DICCIONARIO TENDRA COMO VALORES , LISTAS
#creamos el diccionario vacio
diccionario_con_arreglo = {}
#agregamos la llave salarios_tipo1 cuyo valor es un arreglo
diccionario_con_arreglo["salarios_tipo1"] = [900000, 1200000]
#agregamos la llave salarios_tipo2 cuyo valor es un arreglo
diccionario_con_arreglo["salarios_tipo2"] = [1500000, 2000000]
#imprimimos nuestro diccionario
print(diccionario_con_arreglo)
#extraemos el elemento de indice 1 del valor de la llave salarios_tipo1, 1200000
print("1200000 como elemento interno: ", diccionario_con_arreglo["salarios_tipo1"][1])
#extraemos el elemento de indice 0 del valor de la llave salarios_tipo2, 1500000
print("1500000 como elemento interno: ", diccionario_con_arreglo["salarios_tipo2"][0])
print("------dicionarios como valores------------")
#ESTE DICCIONARIO TENDRA COMO VALORES OTROS DICCIONARIO
#creamos el diccionario
diccionario_con_diccionario = {
                                "capitales1": {"quindio": "armenia"}, 
                                "capitales2": {"valle": "cali", "antioquia": "medellin"}
                                }
#Leemos el valor de la llave capitales1 y de ese valor leemos el valor de la llave
#quindio
print("esperamos armenia :", diccionario_con_diccionario["capitales1"]["quindio"])
#Leemos el valor de la llave capitales2 y de ese valor leemos el valor de la llave
#atioquia
print("esperamos medellin :", diccionario_con_diccionario["capitales2"]["antioquia"])

print("------recorrido--------")
diccionario_usuarios = {12451: "Pepe Perez", 5415421: "Maria Velez"}
#para recorrer usamos for-in
for llave in diccionario_usuarios:
    print("-------------------")
    print("llave: ", llave)
    print("valor: ", diccionario_usuarios[llave])
    print("-------------------")

#obtener las llaves con metodo .keys()
print("-------llaves obtenidas con .keys()----------")
for key in diccionario_usuarios.keys():
    print("key: ", key)

#obtener los valores con metodo .values()
print("-------valores obtenidos con .values()----------")
for value in diccionario_usuarios.values():
    print("value: ", value)

print("-------objetos permitidos como llaves----------")
#llaves: mutabilidad, inmutabilidad
#SI INTENTAMOS PASAR COMO LLAVE DE UN DICCIONARIO UN OBJETO MUTABLE
#PYTHON NO NOS DEJARAejemplo interpolacion python plantilla
#lista_llave = [1, 2]
#diccionario_1 = {"nombre": "Raul Perez", lista_llave: "Maria Perez"}



