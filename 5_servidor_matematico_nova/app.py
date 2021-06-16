# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

### FUNCIONES DE UTILIDAD
def mostrar_mensaje(mensaje):
    return mensaje
    # respuesta = f"""{mensaje}
    # <br>
    # <br>
    # <button onclick='window.history.back()'>Calcular otro valor</button>
    # <br>
    # <a href='/'>
    # <button>Regresar al menú principal</button>
    # </a>"""
    # return respuesta

### RUTAS QUE SIRVEN LAS INTERFACES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interfaz_suma')
def interfaz_suma():
    return render_template('a_1_suma.html')

@app.route('/interfaz_resta')
def interfaz_resta():
    return render_template('a_2_resta.html')

@app.route('/interfaz_multiplicar')
def interfaz_multiplicar():
    return render_template('a_3_multiplicar.html')

@app.route('/interfaz_division')
def interfaz_division():
    return render_template('a_4_division.html')

@app.route('/interfaz_modulo')
def interfaz_modulo():
    return render_template('a_5_modulo.html')

@app.route('/interfaz_valor_absoluto')
def interfaz_valor_absoluto():
    return render_template('a_6_valor_absoluto.html')

@app.route('/interfaz_promedio')
def interfaz_promedio():
    return render_template('a_7_promedio.html')

@app.route('/interfaz_factorial')
def interfaz_factorial():
    return render_template('a_8_factorial.html')

@app.route('/interfaz_moda')
def interfaz_moda():
    return render_template('a_9_moda.html')

@app.route('/interfaz_area_rectangulo')
def interfaz_area_rectangulo():
    return render_template('b_1_area_rectangulo.html')

@app.route('/interfaz_perimetro_triangulo')
def interfaz_perimetro_triangulo():
    return render_template('b_2_perimetro_triangulo.html')

@app.route('/interfaz_area_triangulo')
def interfaz_area_triangulo():
    return render_template('b_3_area_triangulo.html')

@app.route('/interfaz_perimetro_rectangulo')
def interfaz_perimetro_rectangulo():
    return render_template('b_4_perimetro_rectangulo.html')

@app.route('/interfaz_area_circulo')
def interfaz_area_circulo():
    return render_template('b_5_area_circulo.html')

@app.route('/interfaz_circuferencia_circulo')
def interfaz_circuferencia_circulo():
    return render_template('b_6_circunferencia_circulo.html')

@app.route('/interfaz_volumen_esfera')
def interfaz_volumen_esfera():
    return render_template('c_1_vol_esfera.html')

@app.route('/interfaz_volumen_cubo')
def interfaz_volumen_cubo():
    return render_template('c_2_vol_cubo.html')

#RUTAS QUE REALIZAN LA LOGICA
@app.route('/a_1_suma', methods=['POST'])
def suma():
    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    suma = int(numero1) + int(numero2)
    mensaje = f"La suma de {numero1} y {numero2} es : {suma}"
    return mostrar_mensaje(mensaje)

@app.route('/a_2_resta', methods=['POST'])
def resta():
    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    resta_num = int(numero1) - int(numero2)
    mensaje = "La resta de {} y {} es : {}".format(numero1,numero2, resta_num)
    return mostrar_mensaje(mensaje)


@app.route('/a_3_multiplicar', methods=['POST'])
def multiplicar():
    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    proceso = int(numero1) * int(numero2)
    mensaje = f"El resultado de {numero1} * {numero2} es: {proceso} "
    return mostrar_mensaje(mensaje)

@app.route('/a_4_division', methods=['POST'])
def division():
    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')
    numero1 = float(numero1)
    numero2 = float(numero2)
    if numero2 == 0:
        return mostrar_mensaje(f"El resultado de la division {numero1} / {numero2} es : Indeterminado")
    division = round(numero1 / numero2, 2)
    return mostrar_mensaje(f"El resultado de la division {numero1} / {numero2} es : {division}")

@app.route('/a_5_modulo', methods=['POST'])
def modulo():
    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    numero1 = int(numero1)
    numero2 = int(numero2)
    modulo = numero1 % numero2
    mensaje = f"El módulo de los números {numero1} y {numero2} es : {modulo}"
    return mostrar_mensaje(mensaje)

@app.route('/a_6_valor_absoluto', methods=['POST'])
def valor_absoluto():
    numero = request.form.get("numero")
    entero_numero = int(numero)
    if entero_numero >= 0:
        resultado = entero_numero
    else:
        resultado = -entero_numero
    mensaje = "El valor absoluto del número {} es : {}".format(entero_numero,resultado)
    return mostrar_mensaje(mensaje)

# se declara la ruta 
@app.route('/a_7_promedio', methods=['POST'])
def promedio():
    numeros = request.form.get("numeros")
    numeros = numeros.split(",")
    numeros = list(map(float,numeros))
    resultado = sum(numeros)/(len(numeros))
    mensaje = f"El promedio de los numeros ingresados es:   {resultado}"
    return mostrar_mensaje(mensaje)

@app.route('/a_8_factorial', methods=['POST'])
def factorial():
    numero = request.form.get('numero')
    numero = int(numero)
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    mensaje = f"El factorial del número {numero} es : {factorial}"
    return mostrar_mensaje(mensaje)

@app.route('/a_9_moda', methods=['POST'])
def moda():
    from statistics import mode
    numeros = request.form.get('numeros')
    numeros = numeros.split(',')
    numeros = list(map(int, numeros))
    moda = mode(numeros)
    mensaje = f"La moda de los números {numeros} es : {moda}"
    return mostrar_mensaje(mensaje)

@app.route('/b_1_area_rectangulo', methods=['POST'])
def area_rectangulo():
    altura = request.form.get("altura")
    base = request.form.get("base")
    multiplicacion = int(altura) * int(base)
    mensaje = f"El area del rectangulo con altura de {altura} y base de {base} es: {multiplicacion}"
    return mostrar_mensaje(mensaje)


@app.route('/b_2_perimetro_triangulo', methods=['POST'])
def perimetro_triangulo():
    lado_1 = request.form.get("lado_1")
    lado_2 = request.form.get("lado_2")
    lado_3 = request.form.get("lado_3")
    perimetro = int(lado_1) + int(lado_2) + int(lado_3)
    mensaje = "El perimetro de un triangulo con sus lado A {}, lado B {}, lado C {} es : {}".format(lado_1,lado_2,lado_3,perimetro)
    return mostrar_mensaje(mensaje)

@app.route('/b_3_area_triangulo', methods=['POST'])
def area_triangulo():
    base = request.form.get("base")
    altura = request.form.get("altura")
    area = (float(base) * float(altura)) / 2
    mensaje = f"El area de este triangulo es: {area}"
    return mostrar_mensaje(mensaje)

@app.route('/b_4_perimetro_rectangulo', methods=['POST'])
def perimetro_rectangulo():
    base = request.form.get("base")
    altura = request.form.get("altura")
    base = float(base)
    altura = float(altura)
    perimetro = base * 2 + altura * 2
    mensaje = f"El perímetro de un rectangulo con base {base} y altura {altura} es : {perimetro}"
    return mostrar_mensaje(mensaje)

@app.route('/b_5_area_circulo', methods=['POST'])
def area_circulo():
    radio = request.form.get("radio")
    pi = 3.14 * 2
    area = int(radio) + float(pi)
    mensaje = f"El area del circulo cuyo radio es {radio} multiplicado por {pi} es : {area}"
    return mostrar_mensaje(mensaje)


@app.route('/b_6_circunferencia_circulo', methods=['POST'])
def circunferencia_circulo():
    diametro_circulo = request.form.get("diametro_circulo")
    circunferencia = int(diametro_circulo) * 3.14
    mensaje = "La circunferencia de un circulo que tiene un diametro {} es : {}".format(diametro_circulo, circunferencia)
    return mostrar_mensaje(mensaje)

@app.route('/c_1_vol_esfera', methods=['POST'])
def vol_esfera():
    from math import pi
    radio = request.form.get("radio")
    volumen = ((4 * pi * (int(radio)**3)) / 3)
    mensaje = f"El volumen de la esfera es : {round(volumen,3)} cm<sup>3</sup>"
    return mostrar_mensaje(mensaje)

@app.route('/c_2_vol_cubo', methods=['POST'])
def vol_cubo():
    lado = request.form.get('numero')
    lado = int(lado)
    volumen = pow(lado, 3)
    mensaje = f"El volumen del cubo de lado {lado} es : {round(volumen, 3)} cm<sup>3</sup>"
    return mostrar_mensaje(mensaje)

app.run(debug = True, port=5000)
