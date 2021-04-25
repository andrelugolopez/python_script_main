#4. Dada la siguiente cadena "Programar es algo genial, todos deberían intentarlo, atrévete!"
#genere el siguiente arreglo ["Programar es algo genial", "todos deberían intentarlo", "atrévete!"]
#usando el método split el cual puede consultar en el siguiente link: 
#https://blog.carreralinux.com.ar/2017/07/uso-split-y-join-python/.. 

cadena = "Programar es algo genial, todos deberían intentarlo, atrévete!"
lista_cadena = cadena.split()
print(f"Cadena convertida en lista: {lista_cadena}")