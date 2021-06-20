# -*- coding: utf-8 -*-
from flask import Flask
import pymysql


app = Flask(__name__)



@app.route('/')
def index():
    return "Bienvenido a nuestra tienda: <a href='/stock' >ver stock</a>"


#consultar todo el stock
@app.route('/stock')
def stock():
    #conexion a la db
    conn = pymysql.connect(
    host="localhost", port=3307, user="root",
    db="tienda"
    )
    #se crea el curson a la db
    cursor = conn.cursor()
    #se ejecuta la consulta de todos los productos
    cursor.execute(
        "SELECT * FROM stock"
    )
    #se recuperan los resultados de la cosnulta, en este caso
    #se recuperan todos los resultados fetchall()
    #si quisieramos recuperar la primera fila obtenida en la consulta
    #usariamos fetchone()
    filas = cursor.fetchall()
    #si hay almenos una fila en la consulta..
    if len(filas) > 0:
        #se imprime cada fila
        for fila in filas:
            print(fila)
    #podemos imprimir filas para analizar la estructura
    #la estructura obetenida es un atupla de tuplas, la
    #cual podriamos pasar a la vista para ser iterada
    print(filas)
    #se cierra la conexion a la base de datos
    conn.close()
    return "ok"


#consultar un producto en particular
@app.route('/producto/<id>')
def producto(id):
    #conexion a la db
    conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="2021", db="tienda"
    )
    #se crea el curson a la db
    cursor = conn.cursor()
    #se ejecuta la consulta de todos los productos
    cursor.execute(
        "SELECT nombre,precio FROM stock WHERE id=%s", (id, )
    )
    #se recuperan los resultados de la cosnulta, en este caso
    #se recupera un resultado, usamos fetchone()
    fila = cursor.fetchone()
    #si hay almenos una fila en la consulta..
    if len(fila) > 0:
        #se imprime la informacion del producto
        print("nombre producto: ", fila[0])
        print("precio producto: ", fila[1])
    #podemos imprimir la info completa del producto
    print(fila)
    #se cierra la conexion a la base de datos
    conn.close()
    return "Producto: {} Precio {}".format(fila[0], fila[1])


#eliminar un producto en particular
@app.route('/borrarproducto/<id>', methods=['POST'])
def borrar_producto(id):
    #conexion a la db
    conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="2021", db="tienda"
    )
    #se crea el curson a la db
    cursor = conn.cursor()
    #se ejecuta el borrado del producto mediante su id
    cursor.execute(
        "DELETE FROM stock WHERE id=%s", (id, )
    )
    #se ejecutan los cambios en la base de datos
    conn.commit()
    #se cierra la conexion a la base de datos
    conn.close()
    return "Producto borrado"


@app.route('/nuevoproducto/<nombre>/<precio>', methods=['POST'])
def nuevo_producto(nombre, precio):
    #conexion a la db
    conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="2021", db="tienda"
    )
    #se crea el curson a la db
    cursor = conn.cursor()
    #se ejecuta la insercion del nuevo producto
    cursor.execute(
        "INSERT INTO stock(nombre, precio) VALUES(%s, %s)", (nombre, precio)
    )
    #se ejecutan los cambios en la base de datos
    conn.commit()
    #se cierra la conexion a la base de datos
    conn.close()
    return "ok"



app.run(debug = True, port=5000)
