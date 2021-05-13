# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)
#con esta llave firmamos las cookies
app.secret_key = '54SF4GHAFHGAS4'
productos_user = {}


#RUTAS QUE SIRVEN LAS INTERFACES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interfazresta')
def interfaz_resta():
    return render_template('resta.html')

@app.route('/interfazvalorabsoluto')
def interfaz_valor_absoluto():
    return render_template('valor_absoluto.html')

@app.route('/interfazperimetrotriangulo')
def interfaz_perimetro_triangulo():
    return render_template('perimetro_triangulo.html')

@app.route('/interfazcircuferenciacirculo')
def interfaz_circuferencia_circulo():
    return render_template('circunferencia_circulo.html')


#RUTAS QUE REALIZAN LA LOGICA

@app.route('/resta', methods=['POST'])
def resta():
    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    resta_num = int(numero1) - int(numero2)
    mensaje = "La resta de {} y {} es : {}".format(numero1,numero2, resta_num)
    return mensaje


@app.route('/valor_absoluto', methods=['POST'])
def valor_absoluto():
    numero = request.form.get("numero")
    entero_numero = int(numero)
    if entero_numero >= 0:
        resultado = entero_numero
    else:
        resultado = -entero_numero
    mensaje = "El valor absoluto del número {} es : {}".format(entero_numero,resultado)
    return mensaje

@app.route('/perimetro_triangulo', methods=['POST'])
def perimetro_triangulo():
    lado_1 = request.form.get("lado_1")
    lado_2 = request.form.get("lado_2")
    lado_3 = request.form.get("lado_3")
    perimetro = int(lado_1) + int(lado_2) + int(lado_3)
    mensaje = "El perimetro de un triangulo con sus lado 1 {}, lado 2 {}, lado 3 {} es : {}".format(lado_1,lado_2,lado_3,perimetro)
    return mensaje

@app.route('/circunferencia_circulo', methods=['POST'])
def circunferencia_circulo():
    diametro_circulo = request.form.get("diametro_circulo")
    circunferencia = int(diametro_circulo) * 3.14
    mensaje = "La circunferencia de un circulo que tiene un diametro {} es : {}".format(diametro_circulo, circunferencia)
    return mensaje








"""
@app.route('/login', methods=['POST'])
def login():
    password = request.form.get("password")
    email = request.form.get("email")
    if password == "12345" and email == "test@gmail.com":
        return "login ok", 200
    return "", 403        
"""

"""
Andrea
> Restar 2 numeros
> Valor absoluto de un número
> Perímetro de un rectángulo
> Circunferencia de un círculo
"""


app.run(debug = True, port=5000)
