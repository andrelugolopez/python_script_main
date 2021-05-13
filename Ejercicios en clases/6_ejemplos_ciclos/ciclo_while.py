#CICLO WHILE: LO USAMOS CUANDO NO SABEMOS EXACTAMENTE
#EL NUMERO DE ITERACIONES QUE SE DEBEN HACER
#FUNCIONA CON UNA CONDICION


print("-----numeros del 0 al 20--------------")
#variable control del ciclo, se encarga de garantizar

#sintaxis: se una la plabra reservada while
#while --> mientras que se cumpla la condicion..
#enseguida del while viene la condicion, si la condicion
#se cumple, entramos a iterar.
#que el ciclo no sera un ciclo infinito
x = 0
#aca la condicion es que x <= 20
#el ciclo while puede o no ejecutarse de acuerdo a la condicion
#aca la condicion se cumple, por tanto, entramos a iterar
while x <= 50:
    print(x)
    #la variable control del ciclo debe sufrir 
    #un cambio para garantizar que la condicion
    #no se cumpla alguna vez y salir del ciclo
    x = x + 1
