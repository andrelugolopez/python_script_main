# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)
#app.secret_key = "my"


@app.route('/')
def index():
    return "ok"

@app.route('/miscompras')
def compras():
    return "Tienes 5 compras este mes mayo"

@app.route('/quienes_somos')
def quienes_somos():
    return "SOMOS ADSI RAPPI 2021 Y PROGRAMAMOS"


app.run(debug = True, port=5000)
