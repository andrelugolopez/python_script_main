# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify


app = Flask(__name__)

#UN SERVER CON MULTIPLES FORMAS DE RECIBIR INFORMACIÓN


#RECIBIENDO FORMULARIOS
"""
Espera: formulario con 
    name: cedula int
    name: correo email
    name: password alphanumeric
"""
@app.route('/formulario', methods=['POST'])
def registro_formulario():
    cedula = request.form["cedula"]
    correo = request.form["correo"]
    password = request.form["password"]
    return jsonify({"status": "Registro con formulario ok", "datos": [cedula, correo, password]}), 200


#RECIBIENDO JSON
"""
Espera: json con 
    propiedad: cedula int
    propiedad: correo email
    propiedad: password alphanumeric
"""
@app.route('/json', methods=['POST'])
def registro_json():
    content = request.get_json()
    cedula = content["cedula"]
    correo = content["correo"]
    password = content["password"]
    return jsonify({"status": "Registro con json ok", "datos": [cedula, correo, password]}), 200


#RECIBIENDO PARAMETROS EN LA RUTA. LOS PARAMETROS EN LA RUTA MODIFICAN LA URL
"""
Espera: parametros de ruta con 
    valor: cedula int
    valor: correo email
    valor: password alphanumeric
"""
@app.route('/parametrosruta/<cedula>/<correo>/<password>', methods=['POST'])
def registro_parametros_ruta(cedula, correo, password):
    cedula = cedula
    correo = correo
    password = password
    return jsonify({"status": "Registro con parametros de ruta ok", "datos": [cedula, correo, password]}), 200


#RECIBIENDO PARAMETROS DE CONSULTA (STRING QUERY). ESTOS PARAMETROS NO MODIFICAN LA URL
"""
Espera: parametros de consulta
    name: cedula int
    name: correo email
    name: password alphanumeric
"""
@app.route('/parametrosconsulta', methods=['POST'])
def registro_parametros_consulta():
    cedula = request.args.get("cedula")
    correo = request.args.get("correo")
    password = request.args.get("password")
    return jsonify({"status": "Registro con parametros de consulta ok", "datos": [cedula, correo, password]}), 200


#RECIBIENDO CABECERAS
"""
Espera: cabeceras (headers)
    name: cedula int
    name: correo email
    name: password alphanumeric
"""
@app.route('/cabeceras', methods=['POST'])
def registro_cabeceras():
    cedula = request.headers.get("cedula")
    correo = request.headers.get("correo")
    password = request.headers.get("password")
    return jsonify({"status": "Registro con cabeceras ok", "datos": [cedula, correo, password]}), 200





app.run(debug = True, port=5000)
