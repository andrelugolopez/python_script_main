# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for


pais = "Colombia"
ciudad = "Armenia"
direccion = "Barrio Galan"

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', usuario=False)


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template('ubicacion.html',
                            usuario = email,
                            pais_tienda = pais,
                            ciudad_tienda = ciudad,
                            direccion_tienda = direccion
                            )



app.run(debug = False, port=5000)

