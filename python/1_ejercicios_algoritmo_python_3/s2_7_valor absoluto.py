#7. Cree un programa que tome un número real e imprima su valor absoluto. Use funciones. Haga pruebas de escritorio.

'''
pseudo_Algorotmo imprimir_numero_bsoluto

Se recibe el numero por teclado (float)
leer 

se declara la funcion (numero)
    condicion  
    retornar

imprimir resultado

finAlgoritmo
'''

numero = float(input("Ingrese un numero: "))

def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return - numero 
print(f"El valor absoluto del numero {numero} es ")
print ("-->",(valor_absoluto(numero)))




