# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for

compras = []
usuarios = []
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


#esta funcion se encarga de registrar la compra
@app.route('/compra/<producto>', methods=['POST'])
def procesar_compra(producto):
    #se procesa la compra
    compras.append(producto)
    return redirect(url_for('compra_ok', productook=producto))


#esta funcion se encarga unicamente de mostrar mensaje ok al usuario
@app.route('/compraok/<productook>')
def compra_ok(productook):
    return "Producto {} comprado exitosamente".format(productook)


#esta funcion se encarga unicamente de proporcionar la interfaz de registro
@app.route('/registrointerfaz')
def registro_interfaz():
    return render_template('registro.html')


#esta funcion se encarga unicamente deL registro del usuario
@app.route('/registro', methods=['POST'])
def registro():
    nombres = request.form.get("nombres")
    password = request.form.get("password")
    email = request.form.get("email")
    usuarios.append(nombres)
    usuarios.append(password)
    usuarios.append(email)
    return "Registrado con {} y {}".format(nombres, email)



#esta funcion se encarga unicamente de proporcionar la interfaz de registro
@app.route('/masvendido')
def mas_vendido():
    return render_template('vendido.html')





app.run(debug = False, port=4998)

