from flask import Flask, redirect, request, render_template, url_for

app = Flask("tienda_equipos")

@app.route('/', methods=['GET'])
def get_interface_home():
    return render_template('home.html')

@app.route('/perifericos', methods=['GET'])
def get_interface_perifericos():
    perifericos = [
        {"id": 1, "NOMBRE": "TECLADO", "PRECIO": 100000, "STOCK": 4}, 
        {"id": 2, "NOMBRE": "MOUSE", "PRECIO": 30000, "STOCK": 2},
        {"id": 3, "NOMBRE": "DIADEMA", "PRECIO": 150000, "STOCK": 7}
    ]
    return render_template('perifericos.html', elegir_periferico=perifericos)


@app.route('/equipos', methods=['GET'])
def get_interface_equipos():
    equipos = [
        {"clase_equipo": "PC1", "RAM": "8GB", "PRECIO": 2000000},
        {"clase_equipo": "PC2", "RAM": "16GB", "PRECIO": 3500000},
        {"clase_equipo": "PORTATIL", "RAM": "8GB", "PRECIO": 1800000}
    ]
    return render_template('equipo.html', elegir_equipo=equipos)


@app.route('/welcome', methods =['POST'])
def interface_welcome():
    email = request.form.get("email")
    password = request.form.get("password")
    nombre = request.form.get("nombre")
    return render_template('welcome.html', nombre_usuario = nombre, email_usuario = email)








app.run(debug=True, port=5000)