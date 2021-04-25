#3. Dado el siguiente arreglo [ "Colombia", "es", "un", "país", "extraordinario" ],
#imprima en consola el mensaje "Colombia es un país extraordinario" usando el método join
#el cual puede consultar en el siguiente link: https://blog.carreralinux.com.ar/2017/07/uso-split-y-join-python/. 

frase = [ "Colombia", "es", "un", "país", "extraordinario" ]
frases_string = ','.join(frase)
print(f"Impresión de arreglo con método join: {frases_string}" )
