#CICLOS (ESTRUCTURAS DE REPETICION): SE USAN CUANDO 
#NECESITAMOS ITERAR, REPETIR INSTRUCCIONES VARIAS VECES.

#CICLO for
#LO USAMOS CUANDO VAMOS A REPETIR UN NUMERO DE VECES CONOCIDO

print("-----numeros del 0 al 20--------------")
#imprimir los numeros del 0 al 20:
#sintaxis: se usa la palabra reservada for
#se lee para cada..
#el i en este caso se le puede llamar la variable de iteracion
#no es obligatorio que la varibale de iteracion se llame i
#todo se lee: para cada i en el rango de 0 a 21 sin tomar el 21
#haga. No olvidar que los dos puntos
#aca, el 0 es el limite inferior y el 21 el limite superior del for
#el limite superior no se toma

#i varia de 0 a 20
for i in range(0, 21):
    #bloque de instrucciones del for
    #deja de ejecutarse cuando las iteraciones terminan
    print(i)

print("-----numeros del 0 al 9--------------")
#imprimir los numeros enteros de 0 a 9
#aca obviamos el limite inferior que por defecto es 0
for i in range(10):
    print(i)

print("-----variacion de la variable de iteracion--------------")

for i in range(10, 21):
    print(i)

print("-----con base en i, mostrar los numeros del 10 al 20 aumentados en 2--------------")
for i in range(10, 21):
    print(i + 2)
   