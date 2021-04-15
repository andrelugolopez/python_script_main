print("------condicional doble 1 ----------")
#el igual es el operador de
#asigancion
x = 8
#si x es igual a 10...
if x == 10:
    print("X es igual a 10")
    #en caso contrario(si x no es igual a 10)
else:
    #bloque de instrucciones del else
    print("X No es igual a 10")

print("------condicional doble 2 ----------")
#saber si una persona es mayor de edad o no
edad = 25
#si la persona es mayor de edad...
if edad >= 18:
    print("Ud es mayor de edad")
else:
    print("Ud No es mayor de edad")

print("------condicional doble 3 ----------")
estrato = int(input("ingrese estrato"))
edad = int(input("ingrese edad"))
#si el estrato es 1 y es mayor de edad...
if estrato == 1 and edad >= 18:
    print("Tiene derecho a subsidio")
else:
    print("No Tiene derecho a subsidio")


