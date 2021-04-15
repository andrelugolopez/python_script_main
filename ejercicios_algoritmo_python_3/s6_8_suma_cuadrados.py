#8. Cree un programa que calcule la suma de los cuadrados de los números entre 1 y n. Use ciclo while.
#Use funciones. Haga pruebas de escritorio. 
def sumar_cuadrados_numeros(numero_usuario):   
    x = 0
    total = 0
    while x <= numero_usuario:        
        total = total + x**2
        x = x + 1
    return total
try:
    numero_usuario = int(input("Ingrese número hasta donde se va hacer la suma de los cuadrados: "))
except:
    print("ERROR: Se permiten solo números enteros porque el ciclo es 1 + 1")
    exit()
total = sumar_cuadrados_numeros(numero_usuario)
print(f"La suma de los cuadrados es: {total}")




