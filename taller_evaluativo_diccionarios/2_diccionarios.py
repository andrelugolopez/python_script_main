#2. Dado el siguiente diccionario:
# persona = {"edad": 20, "peso": 75, "nombres": "Pedro", "apellidos": "Pérez Pérez"};
#Consulte por los métodos keys() y values() en la página: 
#https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/tipo_diccionarios.html

print("-----------------------------------------")
#usando ciclo for y el método keys(), imprima todas las claves del diccionario dado

persona = {"edad": 20, "peso": 75, "nombres": "Pedro", "apellidos": "Pérez Pérez"}
print("Imprimir llaves del diccionario con ciclo for: ")
informacion_persona = persona.keys()

for llaves in informacion_persona:
    print(llaves)

print("-----------------------------------------")
# usando ciclo for y el método values() imprima todos los valores del diccionario.
print("Imprimir valores del diccionario con ciclo for: ")

informacion_persona = persona.values()

for valores in informacion_persona:
    print(valores)

# Luego, sobre el mismo diccionario realice las siguientes operaciones: 

print("-----------------------------------------")
#● Cambie el valor de la clave peso por 77
print(f"Diccionario original: {persona}")
persona["peso"] = 77
print(f"Diccionario cambio de peso a 77: {persona}")

print("-----------------------------------------")
#● Cambie el valor de la clave edad por 21 
print(f"Diccionario antes del cambio: {persona}")
persona["edad"] = 21
print(f"Diccionario cambio de edad a 21: {persona}")

print("-----------------------------------------")
#● Elimine la clave apellidos usando método pop 
print(f"Diccionario antes de eliminar apellidos: {persona}")
persona.pop("apellidos")
print(f"Diccionario con eliminación de clave apellidos {persona}")

print("-----------------------------------------")
#● Imprim el valor de la clave peso usando el método get
print(f"Impresión de diccionario del valor de la clave peso: {persona.get('peso')}")



