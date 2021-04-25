#2. Cree un programa que almacene los documentos y nombres de diez usuarios,
#donde a cada documento corresponda su respectivo nombre. Use diccionarios
# Imprima todos los nombres de los usuarios usando el ciclo for. 


usuarios =  {
              1546828 : "Andrea",
              2056242 : "Pablo",
              8976646 : "Oscar",
              5666444 : "Andres",
              563189 : "Felipe",
              4661131 : "Carolina",
              7892121 : "Marcela",
              7777777 : "Camilo",
              205656 : "Cesar",
              9685656 : "Natalia",
            }

lista_usuarios = usuarios.values()

for usuario in lista_usuarios:
    print(usuario)




"""
diccionario_nombres = {}
for i in range(10):
    numero_identificacipn = input("Ingreses su numero de identificación:")
    nombre = input("Ingrese su nombre: ")
    diccionario_nombres[numero_identificacipn] = nombre

print("lista de nombres: ")
for llave in diccionario_nombres:
    print(diccionario_nombres[llave])
print("-------------------------------------")
"""


