from flask import Flask, redirect, request, render_template, url_for
# flask es el módulo donde está todo lo relacionado a Flask

# Instalación de Flask
# consola
# >> pip3 install flask

# Flask es una librería Backend

# Creo una lista vacía para guardar los animales adoptados
animales = []

# Creo mi aplicación de Flask con un nombre
app = Flask("tienda_mascotas")

# @app.route([ruta del navegador], [método de envio = GET])
# ruta del navegador siempre empieza con /
# el método de envio es GET por defecto

# @app.route(...)
# def funcion():
#   ...
#   return "ok"

# La función es la que responde a la ruta

# Cuando escribimos en el navegador
# localhost = 127.0.0.1

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/gatos')
def get_interfaz_gatos():
    return render_template('gatos.html')

@app.route('/perros')
def get_interfaz_perros():
    return render_template('perros.html')

@app.route('/inicio_sesion')
def get_interfaz_inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/donaciones')
def get_interfaz_donaciones():
    return render_template('donaciones.html')
    
### RUTAS QUE CORRESPONDE A LA LÓGICA DEL NEGOCIO
# Toda aquella lógica que responde a procesos

# /adopcion_correcta/<animal>
# /adopcion_correcta/cocodrilo
# /adopcion_correcta/tigre

# Recibimos los datos por la ruta
@app.route('/adopcion_correcta/<animal>')
def get_adopcion_correcta(animal):
    return f'Has adoptado correctamente a el animal: {animal}'

# Recibimos los datos por formulario
@app.route('/login', methods=['POST'])
def post_login():
    usuario = request.form.get('username')
    password = request.form.get('password')
    print(f"Los datos ingresados fueron: {usuario} y {password}")
    return redirect(url_for('get_inicio_sesion_correcto', usuario=usuario))

# Recibimos los datos por la ruta y por consulta

# /adoptar/perro?id=5
# /adoptar/gato?id=2
# /adoptar/guacamaya?id=10
# /adoptar/perro?id=6
# Perro 6

# /adoptar/perro1
# /adoptar/perro2

@app.route('/adoptar/<animal>')
def post_adoptar(animal):
    id = request.args.get('id')
    animal_id = f"{animal}_{id}"
    animales.append(animal_id)
    return redirect(url_for('get_adopcion_correcta', animal=animal_id))

@app.route('/inicio_sesion_correcto/<usuario>')
def get_inicio_sesion_correcto(usuario):
    return f'¡Has iniciado sesión exitosamente {usuario}!'

app.run(debug=True, port=5000)
