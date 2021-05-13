contador = 10

def aumento():
    indice = 1
    global contador
    contador = contador + indice
    return(contador)

print(aumento())