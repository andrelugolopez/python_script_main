# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for

productos_stock = {"1": "Leche", "2": "Arroz", "3": "Aceite", "4": "Lentejas"}

lista_sucursales = [
               ["Bogota", "65845456"],
               ["Cali", "6545665"],
               ["Medellin", "125686"],
               ["Armenia", "6356554"],
               ["Santa Marta", "655478514"],
               ["Cartago", "21254654"]
               ]

lista_productos = [
    ["Leche", "2000", "producto1.jpg", "1"],
    ["Arroz", "2000", "producto2.jpg", "2"],
    ["Aceite", "10000", "producto3.jpg", "3"],
    ["Lentejas", "1800", "producto4.jpg", "4"]
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comprar/<id>')
def procesar_compra(id):
    nombre_producto = productos_stock[id]
    return "Compra realizada del producto con nombre {}".format(nombre_producto)


@app.route('/productos')
def productos():
    
    return render_template('productos.html', productos_=lista_productos)


@app.route('/sucursales')
def sucursales():
    
    return render_template('sucursales.html', sucursales_=lista_sucursales)






app.run(debug = False, port=5000)

