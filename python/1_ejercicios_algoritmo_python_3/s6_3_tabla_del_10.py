#3. Cree un programa que muestre la tabla de multiplicar del 10, del 1 al 50. Use ciclo while.
# Use funciones. Haga pruebas de escritorio. 

limite = 50
def tabla_del_diez(numero):
    x = 1
    while x <= limite:
        resultado_tabla = x * 10
        print(f" 10 x {x} = {resultado_tabla}")
        x = x + 1
tabla_del_diez(limite)