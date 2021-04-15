#3. Cree un programa que calcule el promedio de tres notas para n estudiantes.
#  Use ciclo for. Use funciones. Haga pruebas de escritorio. 

#declarar funcion para que entre por teclado los estudiantes que se desee
def cuantos_estudiantes():
    return int(input("Ingrese los estudiantes que desee -> "))
print("-----------------------------------")


#declarar funcion para que itere los numeros de estudiantes que deseo
def estudiantes(cuantos_estudiantes):
    if cuantos_estudiantes > 0:
        #se declara una lista donde se alamacenan las listas de las notas
        nota_lista = []
        for i in range (cuantos_estudiantes):       
            print(f"{i+1}. Estudiante ")
            #se crea una lista donde guarde las notas de los estudiantes 
            notas = []
            #se anida el for dentro del for 
            for i in range(3):      
                nota_actual = float(input("Ingrese una nota: "))       
                #las notas ingresadas actuales se guardaran en la lista (notas)  
                notas.append(nota_actual)      
            '''la lista de (notas) de cada estudiante se guardan en la lista (nota_lisa)'''    
            nota_lista.append(notas)
        #se retorna nota_lista para que asi tenga listas dentro de una lista 
        return nota_lista  
    else: 
        print("Ingrese un numero valido 'positivo'")    

#funcion para saber el promedio de las notas
def promedio(estudiantes):
    #se crea unq lista para alamcenar los promedios 
    lista_promedios = []    
    #for para tomar tomar la listas de notas de la lista
    for notas in estudiantes:
        #se declara la variable (suma) para que despues se puedan sumar las notas
        suma = 0
        #for para tomar cada nota de la lista
        for cada_nota in notas:
            suma += cada_nota
        resultado_promedio = round(suma / 3)
        #se añaden los promedios de las notas de cada estudiante a la (lista_promedios)
        lista_promedios.append(resultado_promedio)
    return lista_promedios

#llamar funciones
cuantos = cuantos_estudiantes()
print("----------------------")
datos_lista = estudiantes(cuantos)
print("----------------------")
final_promedio = promedio(datos_lista)
print(f"Promedio: {final_promedio}")
