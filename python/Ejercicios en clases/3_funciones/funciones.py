print("------funcion con un parametro------")
#para crear una funcion usamos def
#los parametros se definen dentro de los
#parentesis. Siempre se finaliza la definicion
#de la funcion con :
#esta funcion tiene un parametro x
def lineal(x):
    suma = x + 2 #bloque de instrucciones
    return suma #retorno


#para llamar a una funcion
#lo hacemos por su nombre usando tambien
#() Si la funcion no se llama no trabaja
#se sugiere guardar los valores devueltos
#por una funcion en una variable
#aca el 50 se llama argumento
valor_devuelto = lineal(50)
print("El valor devuelto por lineal es: ", valor_devuelto)

print("------funcion sin parametros------")
#no siempre es necesario que una funcion tenga
#argumentos
def mensaje_adsi():
    mensaje = "SOMOS ADSI RAPPI 2021"
    return mensaje

#llamada a la funcion mensaje_adsi
mensaje_funcion = mensaje_adsi()
print("El mesaje es: ", mensaje_funcion)

print("------funcion con parametros por defecto------")

#aca peso y aceleracion son parametros obligatorios
#y gravedad tiene un valor por defecto, si se pasa gravedad
#se trabaja con el valor pasado como argumento, 
#de lo contrario se trabaja con su valor por defecto o sea 980
#PRIMERO VAN LOS PARAMETROS OBLIGATORIOS Y LUEGO LOS CON VALORES POR DEFECTO
#SE PUEDEN TENER VARIOS OBLIGATORIOS Y VARIOS POR DEFECTO
def gravedad_simulacion(peso, aceleracion, gravedad=980):
    mensaje = "Peso: {} Acele: {} Gravedad: {}".format(peso, aceleracion, gravedad)
    return mensaje

#llamado a la funcion gravedad_simulacion
#aca solo estamos obligados a pasar peso y aceleracion
valor_funcion_gravedad = gravedad_simulacion(10, 2)
print("Valor funcion gravedad: ", valor_funcion_gravedad)
#aca pasamos gravedad para no usar el valor por defecto
valor_funcion_gravedad_2 = gravedad_simulacion(5, 1, 780)
print("Valor funcion gravedad: ", valor_funcion_gravedad_2)



