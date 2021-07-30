from flask import Flask, render_template, request, redirect, url_for, session, make_response
import pymysql
import ast

app = Flask("APP finanzas")

# cookie
### ESTA ES LA LLAVE QUE SE UTILIZA PARA ---> ENCRIPTAR Y DESEMCRIPTAR
app.secret_key = "a5jgrt8lodGGG55G7H8U5J11DED6SXCD"

# (BASES DE DATOS)
# 1--> Diccionario que guarda a los usuarios registrados 
usuarios = {}

# 2--> Diccionario que guarda las tarjetas creada (Fijos)

# [categorias.id, categorias.nombre, categorias.idusuario] 
# [descripciones.id, descripciones.detalle, descripciones.valor, descripciones.idcategoria]
#lista_tarjetas = [  ["01","1",'servicios','Energia',300,'Agua',500], 
#                    ["02","1",'transporte','bus',1000]
#                    
#                ]

lista_tarjetas = [  ["A01", "1", "Servicios"],
                    ["A02", "1", "Transporte"],
                    ["A03", "2", "Inversiones"]]

lista_items_tarjeta = [ ["1",   "A01",  "Energia",          300],
                        ["2",   "A01",  "Agua",             500],
                        ["3",   "A02",  "Bus",              1000],
                        ["4",   "A03",  "Bienes Raices",    2000]]

### LISTA CON DICCIONARIO
# lista_tarjetas = [
#         {
#         "servicios":{"Energia":20.000,"Agua": 50.000,"Gas": 10.000,"Arrendo":60.0000},
#         "compras":{"Ropa":150.000,"Entretenimiento":100.000},
#         "transporte":{"Bus":20.000,"Uber":20.000,"Gasolina":60.000}
#         }        
#     ]

### FUNCIONES PARA DATOS

def crear_conexion():
    HOST = 'localhost'
    PORT = 3306
    USER = 'root'
    PASS = '1234'
    DB = 'app_finanzas'
    return pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        passwd=PASS,
        db=DB,
    );

### FUNCIONES DE APOYO

def construir_datos(idusuario, categorias, descripciones):
    datos = {}
    # Lista de tarjetas que pertenece al idusuario
    tarjetas_usuario = []
    # Recorro las tarjetas
    for categoria in categorias:
        # Obtengo el idusuario en los datos de la tarjeta
        id_usuario_tarjeta = categoria[2]
        if id_usuario_tarjeta == idusuario:
            # Agrego la tarjeta
            tarjetas_usuario.append(categoria)
    # Recorro cada tarjeta del usuario
    for tarjeta_usuario in tarjetas_usuario:
        # Obtengo el id de la tarjeta (A01, A02 etc)
        id_tarjeta = tarjeta_usuario[0]
        nombre_tarjeta = tarjeta_usuario[1]

        valores_tarjeta = []
        # Obtengo los valores de la tarjeta
        for descripcion in descripciones:
            # Obtengo el id de la tabla a la que pertenece el valor
            id_valor_lista = descripcion[3]
            # Si el id coincide con la tarjeta
            if id_valor_lista == id_tarjeta:
                # Lo agrego a la lista de valores
                valores_tarjeta.append(descripcion)

        # Creo el diccionario de valores
        diccionario_valores = {}
        # Registro cada valor en el diccionario
        for valor in valores_tarjeta:
            # Obtengo los datos del valor
            nombre_valor = valor[1]
            costo_valor = valor[2]
            # Agrego los datos al diccionario
            diccionario_valores[nombre_valor] = costo_valor
        
        # Registro la tarjeta en los datos
        datos[nombre_tarjeta] = diccionario_valores

    # print(valores_tarjeta)
    return datos

def calcular_total(tarjetas):
    # Defino el diccionario de salida
    totales = {}
    # Recorro las llaves de tarjeta
    for llave in tarjetas:
        # Defino la variable de total para los items de las tarjetas
        total = 0
        # Obtengo los datos de la tarjeta
        valor_tarjeta = tarjetas.get(llave)
        # Recorro cada uno de los datos de la tarjeta
        for valor in valor_tarjeta.values():
            # Incremento el total con el valor de la tarjeta
            total += valor;

        # Registro el total usando la llave original
        totales[llave] = total
    return totales

def construir_categorias(categorias):
    output = {}
    for categoria in categorias:
        # Obtengo el id de la categoria
        id_categoria = categoria[0]
        # Obtengo el nombre de la categoría
        nombre_categoria =categoria[1]
        # Guardo el nombre y el id en el diccionario
        output[nombre_categoria] = id_categoria
    return output

def formatear_como_moneda(entrada, simbolo='$'):
    valor = "{:,.0f}".format(entrada);
    valor = valor.replace(',','.')
    valor = f'{simbolo}{valor}'
    return valor.replace('{simbolo}-', '−{simbolo}')

### ENRUTAGE
### render_template (MOSTRAR EN PANTALLA)
# Rutas unicamente para mostrar en pantalla --> GET

@app.route('/')
def interfaz_navegacion():
    if "usuario" in session:
        return redirect(url_for('interfaz_workspace'))
    return render_template('landing.html', usuario=session.get('usuario'))

@app.route('/login')
def interfaz_login():
    return render_template('login.html')

@app.route('/registro')
def interfaz_registro():
    return render_template('registro.html')

@app.route('/workspace')
def interfaz_workspace():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    print(session.get('usuario'))
    email = session.get('usuario')
    id_usuario = session.get('id_usuario')
    # Pido la tabla categorías
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute(f'SELECT * FROM categorias WHERE idusuario="{id_usuario}"')
    categorias = cursor.fetchall()
    cursor.execute(f'SELECT id, detalle, valor, idcategoria FROM descripciones')
    descripciones = cursor.fetchall()
    conexion.close()

    tarjetas_usuario = construir_datos(id_usuario, categorias, descripciones)
    total_tarjetas = calcular_total(tarjetas_usuario)
    id_categorias = construir_categorias(categorias)
    # Pedimos el saldo a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT saldo FROM usuarios WHERE email='{email}'")
    saldo = float(cursor.fetchone()[0])
    conexion.close()
    
    saldo_restante = saldo
    suma_tarjetas = 0

    # Recorro las llaves de los totales
    for llave in total_tarjetas.keys():
        # Obtengo el total actual según la llave
        total_actual = total_tarjetas.get(llave)
        # Sumo el total actual
        suma_tarjetas += total_actual
        # Convierto el total para que se muestre como moneda
        total_tarjetas[llave] = formatear_como_moneda(total_actual)

    # Recorro las llaves de las tarjetas de usuario
    for llave in tarjetas_usuario.keys():
        # Obtengo la tarjeta
        item = tarjetas_usuario.get(llave)
        for llave_interna in item:
            # Obtengo el costo de cada item
            costo = item.get(llave_interna)
            # Formateo el costo como moneda
            item[llave_interna] = formatear_como_moneda(costo, simbolo='')

    saldo_restante -= suma_tarjetas
    # print(f'{saldo=}')
    return render_template('workspace.html', tarjetas = tarjetas_usuario, total_tarjetas=total_tarjetas, usuario=session.get('usuario'), saldo=formatear_como_moneda(saldo), saldo_restante=saldo_restante,saldo_restante_en_pantalla=formatear_como_moneda(saldo_restante), costo=formatear_como_moneda(suma_tarjetas), id_categorias=id_categorias)

@app.route('/configuracion')
def interfaz_configuracion():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    return render_template('configuracion.html', usuario=session.get('usuario'))

@app.route('/crear_lista')
def interfaz_crear_lista():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    return render_template('crear-lista.html')

@app.route('/eliminar_lista')
def ruta_eliminar_lista():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    id = request.args.get('id')
    # Elimino el registro de la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute(f'DELETE FROM categorias WHERE id={id}')
    conexion.commit()
    conexion.close()
    return redirect(url_for('interfaz_workspace'))

@app.route('/editar_lista')
def interfaz_editar_lista():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    id_categoria = request.args.get('id_categoria')
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute(f'SELECT nombre FROM categorias WHERE id="{id_categoria}"')
    nombre_categoria = cursor.fetchone()[0]
    # Selecciono las descripciones
    cursor.execute(f'SELECT id, detalle, valor FROM descripciones WHERE idcategoria={id_categoria} LIMIT 4')
    descripciones = cursor.fetchall()
    conexion.close()
    items = ['']*4
    costos = ['']*4
    for i in range(len(descripciones)):
        # Recorro cada descripcion
        descripcion = descripciones[i]
        print(descripcion)
        # Asigno el item y el costo
        items[i] = descripcion[1]
        costos[i] = descripcion[2]
    # Response
    print(descripciones)
    response = make_response(render_template('editar-lista.html', titulo=nombre_categoria, items=items, costos=costos, id_categoria=id_categoria))
    response.set_cookie('descripciones', repr(descripciones))
    response.set_cookie('id_categoria', id_categoria)
    return response

@app.route('/editar_saldo')
def interfaz_editar_saldo():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    return render_template('editar-saldo.html')

#--------------------------------------
# Esto es para cuando el login no es correcto
# Cuando el usuario ingresa un dato mal (usuario ó contraseña)
@app.route('/error_login')
def interfaz_login_incorrecto():
    return render_template('message.html', title='Credenciales incorrectas', content='Usuario o contraseña incorrectos', ok_url=url_for('interfaz_login'))

# Ruta de cuando el usuario no esta registrado
@app.route('/usuario_no_registrado')
def interfaz_usuario_no_registrado():
    return render_template('message.html', title='Usuario no registrado', content='Este correo no se encuentra asociado en App Finanzas', ok_url=url_for('interfaz_login'))
# Ruta donde se cierra sesion exitosamente
@app.route('/logout_exitoso')
def interfaz_logout_exitoso():
    return render_template('message.html', title='Sesión Cerrada', content='Has cerrado sesión exitosamente.')
#-----------------------------------------------------
### RUTAS // POST

@app.route('/login', methods=['POST'])
def get_login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Obtener los datos del usuario
    conexion = crear_conexion()
    # Obtengo el cursor
    cursor = conexion.cursor()
    # Ejecuto el comando de selección
    cursor.execute(f"SELECT password, id FROM app_finanzas.usuarios WHERE email='{email}'")
    # Obtener los resultados
    resultado = cursor.fetchone()
    # Cerrar la conexion
    conexion.close()
    # Compruebo que si el correo está registrado
    if resultado != None:
        # Obtengo la contraseña de la base de datos
        password_registrada = resultado[0]
        id_usuario = resultado[1]
        # Si la contraseña es correcta
        if password_registrada == password:
            # Si el usuario y contraseña coinciden con los de la BD
            # Se verifica la cookie
            # Se crea una sesion y se envia una cookie al navegador
            session["usuario"] = email
            session["id_usuario"] = id_usuario
            return redirect(url_for('interfaz_workspace'))
        return redirect(url_for('interfaz_login_incorrecto'))
    return redirect(url_for('interfaz_usuario_no_registrado'))

@app.route('/registro', methods=['POST'])
def get_registro():
    # Obtengo los valores de registro
    nombres = request.form.get("nombres")
    apellidos = request.form.get("apellidos")
    email = request.form.get("email")
    password = request.form.get("password")

    # TODO: Verificar que el correo no esté ya registrado
    # Crear la conexión
    conexion = crear_conexion()
    # Obtener el cursor
    cursor = conexion.cursor()
    # Ejecutar el comando
    cursor.execute(f"insert into usuarios(nombres, apellidos, email, password) values('{nombres}', '{apellidos}', '{email}', '{password}')")
    # Hacer efectivo el registro
    conexion.commit()
    # Cerrar la conexión
    conexion.close()

    ## Se verifica si el correo ya esta registrado previamnete 
    # if email ==

    return redirect(url_for('interfaz_login'))

@app.route('/registrar_tarjeta', methods=['POST'])
def post_registrar_tarjetas():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    descripciones = request.cookies.get('descripciones')
    id_categoria = request.cookies.get('id_categoria')
    # Convierto las descripciones de str a tupla
    descripciones = ast.literal_eval(descripciones)
    # Obtengo el título del formulario
    titulo = request.form.get('titulo-categoria')
    # Obtengo los items del formulario
    item_names = [request.form.get('item-name-1'),
    request.form.get('item-name-2'),
    request.form.get('item-name-3'),
    request.form.get('item-name-4')]
    # Obtengo los costos de los items del formulario
    item_costs = [request.form.get('item-cost-1'),
    request.form.get('item-cost-2'),
    request.form.get('item-cost-3'),
    request.form.get('item-cost-4')]
   
    # Reviso los costos y los convierto a flotante
    for i in range(len(item_costs)):
        costo = item_costs[i]
        # Si el costo está vacío
        if costo == '':
            item_costs[i] = 0
        else:
            # Convierto el valor de costo de str a flotante
            item_costs[i] = float(costo)

    # Creo las listas de actualización y registro
    lista_actualizacion = []
    lista_registro =  []
    lista_eliminacion = []

    # Obtengo la longitud de descripciones
    cantidad_descripciones = len(descripciones)
    # Recorro cada nombre del item
    for i in range(len(item_names)):
        # Obtengo el nombre
        name = item_names[i]
        # Obtengo el costo
        cost = item_costs[i]
        # Busco el nombre en las descripciones
        # Si está, lo actualizo
        # Si no está, lo creo
        
        # Si estoy en un campo no registrado en descripciones
        if i >= cantidad_descripciones:
            # Si el nombre está vacío
            # No registro el nuevo campo
            if name == '':
                continue
            lista_registro.append((name, cost))
        else:
            # Estoy en un registro existente
            
            # Si el nombre no está vacío
            if name != '':
                # Obtengo el registro
                descripcion = descripciones[i]
                # Obtengo el id de la descripcion
                id_descripcion = descripcion[0]
                lista_actualizacion.append((name, cost, id_descripcion))
            else:
                # El nombre está vacío
                # Obtengo el id del registro
                descripcion = descripciones[i]
                id_descripcion = descripcion[0]
                # Lo almaceno para eliminar
                lista_eliminacion.append(id_descripcion)
    
    conexion = crear_conexion()
    cursor = conexion.cursor()
    # Actualizo los datos existentes
    for actualizacion in lista_actualizacion:
        query = f'UPDATE descripciones SET detalle="{actualizacion[0]}", valor={actualizacion[1]} WHERE id={actualizacion[2]}'
        print(query)
        cursor.execute(query)
        conexion.commit()
    # Creo los nuevos datos
    for registro in lista_registro:
        valores = f'"{registro[0]}", {registro[1]}'
        query = f'INSERT INTO descripciones(detalle, valor, idcategoria) VALUES({valores}, {id_categoria})'
        print(query)
        cursor.execute(query)
        conexion.commit()

    # Elimino los datos requeridos
    for eliminacion in lista_eliminacion:
        query = f'DELETE FROM descripciones WHERE id={eliminacion}'
        print(query)
        cursor.execute(query)
        conexion.commit()

    # Actualizo el título de la categoría
    query = f'UPDATE categorias SET nombre="{titulo}" WHERE id={id_categoria}'
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    
    return redirect(url_for('interfaz_workspace'))

@app.route('/crear_tarjeta', methods=['POST'])
def post_crear_tarjeta():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    # Obtengo el título del formulario
    titulo = request.form.get('titulo-categoria')
    id_usuario = session.get('id_usuario')
    # Obtengo los items del formulario
    item_names = [request.form.get('item-name-1'),
    request.form.get('item-name-2'),
    request.form.get('item-name-3'),
    request.form.get('item-name-4')]
    # Obtengo los costos de los items del formulario
    item_costs = [request.form.get('item-cost-1'),
    request.form.get('item-cost-2'),
    request.form.get('item-cost-3'),
    request.form.get('item-cost-4')]
    
    lista_registro = []
    for i in range(len(item_names)):
        name = item_names[i]
        # Le quita los espacios en blanco
        name = name.strip()
        # Si el nombre está vacío
        if name == '':
            continue
        cost = item_costs[i]
        lista_registro.append((name, cost))
    
    # Creo la conexion a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    # Inserto el título
    query = f'INSERT INTO categorias(nombre, idusuario) VALUES("{titulo}",{id_usuario})'
    cursor.execute(query)
    conexion.commit()
    # Selecciono id basado en el título y el idusuario
    query = f'SELECT id FROM categorias WHERE nombre="{titulo}" AND idusuario={id_usuario}'
    cursor.execute(query)
    id_categoria = cursor.fetchone()[0]

    for registro in lista_registro:
        # Inserto las descripciones según el id_categoria
        valores = f'"{registro[0]}", {registro[1]}'
        query = f'INSERT INTO descripciones(detalle, valor, idcategoria) VALUES({valores}, {id_categoria})'
        cursor.execute(query)
        conexion.commit()
    conexion.close()
    return redirect(url_for('interfaz_workspace'))

## Ruta para cerrar sesión

@app.route('/logout')
def cerrar_sesion():
    if "usuario" in session and "id_usuario" in session:
        session.pop("usuario")
        session.pop("id_usuario")
        return redirect(url_for('interfaz_logout_exitoso'))
    return redirect(url_for("interfaz_usuario_no_registrado"))

@app.route('/editar_saldo', methods=['POST'])
def editar_saldo():
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    new_saldo = float(request.form.get("saldo"))
    email = session.get('usuario')
    # Guardar saldo del usuario
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = f'UPDATE usuarios SET saldo={new_saldo} WHERE email="{email}"'
    print(f'{query=}')
    cursor.execute(query)
    conexion.commit()
    conexion.close()
    print(f'{new_saldo=}')
    return redirect(url_for('interfaz_workspace'))

app.run(debug = True, port=5000)

