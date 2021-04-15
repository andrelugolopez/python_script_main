# Cree un programa que lea el monto de un préstamo 
# y el plazo en meses, y muestre al usuario el valor 
# de las cuotas mensuales pagando un interés fijo del 2.7% 
# mensual.

# Algoritmo Intereses
# Entero prestamo, meses
# Real valor_mens, interes_mens, valor
# Constante Real INTERESES = 0.027

# imprimir("Ingrese el monto del préstamo: ")
# leer(prestamo)

# imprimir("¿A cuantas cuotas desea diferir el prestamo?: ")
# leer(meses)

# valor_mens = prestamo / meses
# interes_mens = valor_mens * INTERESES
# valor = interes_mens + valor_mens
# imprimir("VALOR", valor)

#FinAlgoritmo

prestamo = int(input("Ingrese el monto del prestamo: "))
meses = int(input("¿A cuantas cuotas desea diferir el prestamo?: "))
INTERESES = 0.027
valor_mens = prestamo/meses # valor a pagar por mes
interes_mens = valor_mens * INTERESES # valor del interes por mes
valor = interes_mens + valor_mens # esta es la suma del valor y el interes mensual

print("VALOR",valor)
