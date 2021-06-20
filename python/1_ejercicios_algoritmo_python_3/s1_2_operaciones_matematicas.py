#  Cree un programa que lea dos números y
#  muestre su producto, su cociente, su módulo,
#  su suma y su resta.
#  Algoritmo operaciones
    #   Real numero1, numero2,suma, resta, mult, modulo,cociente
    
    #   logico error_division = False
    #   imprimir("Ingrese un numero: ")
    #   leer(numero1)
    #   imprimir("Ingrese otro numero: ")
    #   leer(numero2)
    #   suma = numero1 + numero2
    #   resta = numero1 - numero2
    #   mult = numero1 * numero2
    #   modulo = numero1 % numero2
    #   cociente = numero1 / numero2

    #   imprimir(suma,resta,mult,modulo,cociente)
#FinALgoritmo

numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese otro numero: ")

numero1 = float(numero1)
numero2 = float(numero2)

suma = numero1 + numero2
resta = numero1 - numero2
mult = numero1 * numero2
if numero2 != 0 :#si el numero 2 es distinto a 0
    modulo = numero1 % numero2
    cociente = numero1 / numero2
else : 
    modulo = "indeterminado"
    cociente = "indeterminado"

print(f"la suma de los dos numeros es: {suma}",f"la resta de los dos numeros es: {resta}",f"El producto de los dos numeros es: {mult}",f"El modulo de los dos numeros es: {modulo}",f"El cociente de los dos numeros es: {cociente}",sep="\n")

