#LISTAS: conjunto de elementos preferiblemente del mismo
#tipo. Los elementos se encuentran ordenados por indice.
#es una estructura de datos.

#sintaxis
#se define el identificador, seguido del operador de
#asignacion =, y entre corchetes [] se ponen los elementos
#separados por ,
#arreglo que contiene numeros
numeros = [13, 14, 15, 200.5, -100]
#arreglo(lista) vacia
lista_vacia = []
print("----lectura----")
#lectura de elementos
#se usa el identificador seguido de corchetes que contienen el
#indice del elemento que se quiere leer
print("elemento de indice 3: ", numeros[3])
print("----asignacion-sobreescritura----")
#para asignar o sobreescribir elementos se usa
#el operador de asignacion =
#aca sobreescribimos el elemento de indice 4
#y le asignamos un nuevo valor 10000
numeros[4] = 10000
print("verificamos si el elemento cambio: ", numeros[4])
print("-------Borrado--------")
print("Arreglo antes del borrado: ", numeros)
#para eliminar usamos el metodo pop evaluandolo en el indice
#del elemnto que queremos eliminar
#aca eliminamos el elemento 10000 cuyo indice es 4
numeros.pop(4)
print("Arreglo despues del borrado: ", numeros)
#aca eliminamos el elemento 14 cuyo indice es 1
numeros.pop(1)
print("Arreglo despues del segundo borrado: ", numeros)
print("-------agregacion de elementos--------")
#para agregar se usa el metodo append evaluado en el nuevo
#elemento que queremos agregar
#aca agragamos el elemento 25
print("Arreglo antes de agregar un elemento: ", numeros)
numeros.append(25)
print("Arreglo despues de agregar un elemento: ", numeros)

#que pasa cuando tratamos de acceder a un indice que no existe?
#aca tratamos de acceder al indice 20 de la lista numeros
#numeros[20]
print("---copia de arreglos-----")
#copia de arreglos. Para realizar una copia de arreglos independiente
#debemos usar el metodo copy.
#copia no independiente
edades = [10, 15, 90, 20]
edades_copia = edades
print("contenido antes de modificar edades", edades_copia)
edades.pop(2)
print("contenido despues de modificar edades", edades_copia)
#copia independiente usamos copy()
edades_2 = [100, 12, 19, 5]
edades_copia_2 = edades_2.copy()
print("contenido antes de modificar edades_2", edades_copia_2)
edades_2.pop(2)
print("contenido despues de modificar edades", edades_copia_2)

print("-------operador len--------")
#operador len: nos sirve para saber al ongitud de p.e.
#arreglos, cadenas...
#operador len aplicado a una cadena, devuelve la longitud
#de la cadena, es decir, el numero de caracteres de la cadena
#sintaxis: se una len evaluado en el elemento del cual queremos
#saber su longitud
cadena = "abc  zx"
print("longitud de la cadena: ", len(cadena))
#len aplicado a LISTAS
#devuelve el numero de elementos de la lista
lista_len = [True, "ADSI RAPPI", 10.6, 100]
print("longitud de la LISTA: ", len(lista_len))

print("-----1 for aplicado a un arreglo------")
#imprimir cuatro nombres de personas que esten previamente
#guardadas
#SIN ARREGLOS
#aca tenemos una colecccion de nombres de
nombre1 = "Maria"
nombre2 = "Pedro"
nombre3 = "Raul"
nombre4 = "Luisa"
print(nombre1, nombre2, nombre3, nombre4)
#las colecciones las trabajamos con estructuras de datos
#CON ARREGLOS
arreglo_nombres = ["Maria", "Pedro", "Raul", "Luisa"]
#iteracion sobre el arreglo
for nombre in arreglo_nombres:
    print("nombres: ", nombre)
#iteracion con range, usando len
#nos permite trabajar con el indice
#si eliminamos un elemento el for no tira
#errores, igual si agregamos elementos
#EL LIMITE SUPERIOS EN LOS CICLOS CUANDO RECORREMOS
#ARREGLOS LO DEBEMOS TRABAJAR SUJETO A LA LONGITUD
#DEL ARREGLOS
arreglo_nombres.pop(2)
for i in range(0, len(arreglo_nombres)):
    print("elemento: ", arreglo_nombres[i])

print("----AUMENTAR ELEMENTOS DE UN ARREGLO CON for-----")
#aumentar los elementos del siguiente arreglo en 1
#use for
arreglo_aumento = [5, 6, 7, 8]
for i in range(len(arreglo_aumento)):
    arreglo_aumento[i] = arreglo_aumento[i] + 1
print("arreglo despues de aumento: ", arreglo_aumento)


