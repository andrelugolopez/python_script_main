suma = 0
numero2 = 10
def suma():
    def suma_interna():
        numero1 = 10
        global numero2
        suma = numero1 + numero2
        return suma
    numero2 = 5
    sum_aux = suma_interna()
    return sum_aux

print(suma())