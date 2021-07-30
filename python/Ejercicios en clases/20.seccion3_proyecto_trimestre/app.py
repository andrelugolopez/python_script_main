# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for, session

#guarda los usuarios registrados en nuestro sitio
usuarios = {}


#MODEL
#contiene la descripcion de los productos
productos_stock = {"1": "Leche", "2": "Arroz", "3": "Aceite", "4": "Lentejas"}

#contiene la descripcion de las sucursales
lista_sucursales = [
                    ["Bogota", "65845456"],
                    ["Cali", "6545665"],
                    ["Medellin", "125686"],
                    ["Armenia", "6356554"],
                    ["Santa Marta", "655478514"],
                    ["Cartago", "21254654"]
                ]

#contiene descripcion breve de los productos para ser mostrados en la vista
lista_productos = [
                    ["Leche", "2000", "producto1.jpg", "1"],
                    ["Arroz", "2000", "producto2.jpg", "2"],
                    ["Aceite", "10000", "producto3.jpg", "3"],
                    ["Lentejas", "1800", "producto4.jpg", "4"]
                ]



app = Flask(__name__)
#llave con que se firmaran nuestras cookies de sesion
app.secret_key = "ajhsdg56dkgasdhbs"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/interfazlogin')
def interfaz_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    correo = request.form.get('correo')
    password = request.form.get('password')
    #si existe un usuario con el correo enviado por el cliente...
    if usuarios.get(correo):
        #se verifica que el password registrado en la bd
        #coincida con el password enviado por el cliente
        if usuarios[correo]["password"] == password:
            #se crea una sesion y se envia una cookie al cliente con el valor correo
            #este valor queda encriptado mediante la llave configurada anteriormente
            session["usuario"] = correo
            #se pueden agregar varias claves a la cookie
            #por ejemplo para un carrito
            #session["carrito"] = "0"
            return "Has iniciado sesion correctamente"
        return "No has podido iniciar sesion. Usuario o password incorrecto."
    return "No eres un usuario registrado"


@app.route('/interfazregistro')
def interfaz_registro():
    return render_template('registro.html')


@app.route('/registro', methods=['POST'])
def registro():
    #se recuperan los datos del formulario
    correo = request.form.get('correo')
    password = request.form.get('password')
    nombres = request.form.get('nombres')
    apellidos = request.form.get('apellidos')
    #se registran los datos del usuario usando como llave primaria su correo
    usuarios[correo] = {"password": password, "nombres":nombres, "apellidos":apellidos}
    return "registro ok"


@app.route('/logout')
def logout():
    #verificar si el usuario ha enviado una cookie y esta es valida
    #que sea original y que no haya caducado
    if "usuario" in session:
        session.pop("usuario")
        return "Has cerrado sesion"
    return "No tienes una sesion iniciada"


@app.route('/comprar/<id>')
def procesar_compra(id):
    #verificar si el usuario ha enviado una cookie y esta es valida
    #que sea original y que no haya caducado
    if "usuario" in session:
        #extraemos el correo del usuario que llega en la cookie
        correo_cliente = session["usuario"]
        nombre_producto = productos_stock[id]
        return "Compra realizada del producto con nombre {} por el cliente de correo {}".format(nombre_producto, correo_cliente)
    return "Ud no tiene permisos para acceder a este sitio. Por favor inicie sesion"


@app.route('/productos')
def productos():
    return render_template('productos.html', productos_=lista_productos)


@app.route('/sucursales')
def sucursales():
    return render_template('sucursales.html', sucursales_=lista_sucursales)






app.run(debug = False, port=5000)

