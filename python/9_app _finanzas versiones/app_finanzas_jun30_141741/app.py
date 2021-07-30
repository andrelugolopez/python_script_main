from flask import Flask, render_template, request, redirect, url_for, session, make_response
import pymysql
import bcrypt
import ast

app = Flask("APP finanzas")

# cookie
### ESTA ES LA LLAVE QUE SE UTILIZA PARA ---> ENCRIPTAR Y DESEMCRIPTAR
app.secret_key = "a5jgrt8lodGGG55G7H8U5J11DED6SXCD"

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
    # Convierto el número en formato moneda
    valor = "{:,.0f}".format(entrada);
    # Reemplazo las comas por puntos
    valor = valor.replace(',','.')
    # Formateo el valor correctamente
    valor = f'{simbolo}{valor}'
    # Intercambio el signo menos
    return valor.replace(f'{simbolo}-', f'−{simbolo}')

# Rutas unicamente para mostrar en pantalla --> GET

@app.route('/')
def interfaz_navegacion():
    # Hay una sesión de usuario activa
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
    # Hay una sesión de usuario activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    # Obtengo el usuario de la sesión
    email = session.get('usuario')
    id_usuario = session.get('id_usuario')
    # Creo la conexión a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    # Obtengo las categorías
    query = f'SELECT * FROM categorias WHERE idusuario="{id_usuario}"'
    cursor.execute(query)
    categorias = cursor.fetchall()
    # Obtengo las descripciones
    query = 'SELECT id, detalle, valor, idcategoria FROM descripciones'
    cursor.execute(query)
    descripciones = cursor.fetchall()
    # Obtengo el saldo de la base de datos
    cursor = conexion.cursor()
    query = f'SELECT saldo FROM usuarios WHERE email="{email}"'
    cursor.execute(query)
    saldo = float(cursor.fetchone()[0])
    # Cierro la conexión
    conexion.close()
    
    # Construyo los datos que irán en la interfaz
    tarjetas_usuario = construir_datos(id_usuario, categorias, descripciones)
    total_tarjetas = calcular_total(tarjetas_usuario)
    id_categorias = construir_categorias(categorias)

    # Creo las variables de saldo
    saldo_restante = saldo
    suma_tarjetas = 0

    # Recorro las llaves de los totales
    for llave in total_tarjetas.keys():
        # Obtengo el total actual según la llave
        total_actual = total_tarjetas.get(llave)
        # Sumo el total actual
        suma_tarjetas += total_actual
        # Convierto el total para que se muestre como moneda
        total_tarjetas[llave] = formatear_como_moneda(total_actual, simbolo='')

    # Recorro las llaves de las tarjetas de usuario
    for llave in tarjetas_usuario.keys():
        # Obtengo la tarjeta
        item = tarjetas_usuario.get(llave)
        for llave_interna in item:
            # Obtengo el costo de cada item
            costo = item.get(llave_interna)
            # Formateo el costo como moneda
            item[llave_interna] = formatear_como_moneda(costo)

    # Le quito la suma de todas las tarjetas al saldo restante
    saldo_restante -= suma_tarjetas
    return render_template('workspace.html', tarjetas = tarjetas_usuario, total_tarjetas=total_tarjetas, usuario=session.get('usuario'), saldo=formatear_como_moneda(saldo), saldo_restante=saldo_restante,saldo_restante_en_pantalla=formatear_como_moneda(saldo_restante), costo=formatear_como_moneda(suma_tarjetas), id_categorias=id_categorias)

@app.route('/configuracion')
def interfaz_configuracion():
    # Si no hay sesión activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    return render_template('configuracion.html', usuario=session.get('usuario'))

@app.route('/crear_lista')
def interfaz_crear_lista():
    # Si no hay sesión activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    return render_template('crear-lista.html')

@app.route('/eliminar_lista')
def ruta_eliminar_lista():
    # Si no hay sesión activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))

    # Obtengo el id de los argumentos
    id = request.args.get('id')
    # Creo la conexión a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    # Elimino el registro según el id entregado
    query = f'DELETE FROM categorias WHERE id={id}'
    cursor.execute(query)
    conexion.commit()
    # Cierro la conexión a la base de datos
    conexion.close()
    return redirect(url_for('interfaz_workspace'))

@app.route('/editar_lista')
def interfaz_editar_lista():
    # Si no hay sesión activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    # Obtengo el id de la categoría por parámetro de consulta
    id_categoria = request.args.get('id_categoria')
    # Creo la conexión a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    # Obtengo la categoría según el ID
    query = f'SELECT nombre FROM categorias WHERE id="{id_categoria}"'
    cursor.execute(query)
    nombre_categoria = cursor.fetchone()[0]
    # Selecciono las descripciones
    cursor.execute(f'SELECT id, detalle, valor FROM descripciones WHERE idcategoria={id_categoria} LIMIT 4')
    descripciones = cursor.fetchall()
    # Cierro la conexión a la base de datos
    conexion.close()

    # Creo una lista de 4 elementos vacía
    items = ['']*4
    costos = ['']*4
    for i in range(len(descripciones)):
        # Recorro cada descripcion
        descripcion = descripciones[i]
        # Asigno el item y el costo
        items[i] = descripcion[1]
        costos[i] = descripcion[2]
    # Asigno la cookie de descripciones y ID categorias para editar la lista
    response = make_response(render_template('editar-lista.html', titulo=nombre_categoria, items=items, costos=costos, id_categoria=id_categoria))
    response.set_cookie('descripciones', repr(descripciones))
    response.set_cookie('id_categoria', id_categoria)
    return response

@app.route('/editar_saldo')
def interfaz_editar_saldo():
    # Si la sesión de usuario está inactiva
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))
    return render_template('editar-saldo.html')

#--------------------------------------
# Esto es para cuando el login no es correcto
# Cuando el usuario ingresa un dato mal (usuario ó contraseña)
@app.route('/error_login')
def interfaz_login_incorrecto():
    return render_template('message.html', title='Credenciales incorrectas', content='Usuario o contraseña incorrectos', ok_url=url_for('interfaz_login'))

# Ruta para cuando el usuario no esta registrado
@app.route('/usuario_no_registrado')
def interfaz_usuario_no_registrado():
    return render_template('message.html', title='Usuario no registrado', content='Este correo no se encuentra asociado en App Finanzas', ok_url=url_for('interfaz_login'))

# Ruta para cuando tratas de registrar un correo existente
@app.route('/correo_existente')
def interfaz_correo_existente():
    return render_template('message.html', title='Correo Existente', content='El correo ya se encuentra registrado en App Finanzas.', ok_url=url_for('interfaz_registro'))

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
        
        # Convierto el string de la contraseña en bytes
        bytes_pwd = password_registrada.encode('utf8')
        # Si la contraseña es correcta
        if bcrypt.checkpw(password.encode('utf8'), bytes_pwd):
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

    # Crear la conexión
    conexion = crear_conexion()
    # Obtener el cursor
    cursor = conexion.cursor()
    # Obtengo el usuario con el email que me entregaron
    cursor.execute(f'SELECT email FROM usuarios WHERE email="{email}"')
    # Obtengo los resultados
    resultados = cursor.fetchone()
    
    # Si hay al menos un resultado
    # El usuario ya está registrado
    if resultados != None:
        return redirect(url_for('interfaz_correo_existente'))

    # Encripto la contraseña para almacenarla en la base de datos
    # Creo el salt
    salt = bcrypt.gensalt()
    # Obtengo el password en bytes
    bytes_pwd = bytes(str(password), encoding='utf-8')
    # Creo el hash
    # Se hace el decode para transformar bytes en string
    # Y poder guardarlos en la base de datos
    hash_pwd = bcrypt.hashpw(bytes_pwd, salt).decode('utf8')

    # Ejecutar el comando
    cursor.execute(f'insert into usuarios(nombres, apellidos, email, password) values("{nombres}", "{apellidos}", "{email}", "{hash_pwd}")')
    # Hacer efectivo el registro
    conexion.commit()
    # Cerrar la conexión
    conexion.close()

    return redirect(url_for('interfaz_login'))

@app.route('/registrar_tarjeta', methods=['POST'])
def post_registrar_tarjetas():
    # Si el usuario no tiene la sesión activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))

    # Obtengo la descripción y el id de la tarjeta desde la cookie
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

    # Creo la conexión a MySQL
    conexion = crear_conexion()
    cursor = conexion.cursor()

    # limitar el título a 60 caracteres
    titulo = titulo[:60]

    # Actualizo los datos existentes
    for actualizacion in lista_actualizacion:
        query = f'UPDATE descripciones SET detalle="{actualizacion[0]}", valor={actualizacion[1]} WHERE id={actualizacion[2]}'
        cursor.execute(query)
        conexion.commit()

    # Creo los nuevos datos
    for registro in lista_registro:
        valores = f'"{registro[0]}", {registro[1]}'
        query = f'INSERT INTO descripciones(detalle, valor, idcategoria) VALUES({valores}, {id_categoria})'
        cursor.execute(query)
        conexion.commit()

    # Elimino los datos requeridos
    for eliminacion in lista_eliminacion:
        query = f'DELETE FROM descripciones WHERE id={eliminacion}'
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
    # Si el usuario tiene la sesión activa
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
    
    # Obtengo los items de la descripción
    lista_registro = []
    for i in range(len(item_names)):
        # Obtengo el nombre del item
        name = item_names[i]
        # Le quita los espacios en blanco
        name = name.strip()
        # Si el nombre está vacío
        if name == '':
            continue
        # Obtengo el costo del item
        cost = item_costs[i]
        # Registro el item con nombre y costo
        lista_registro.append((name, cost))

    # limitar el título a 60 caracteres
    titulo = titulo[:60]
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

    # Inserto cada registro en la base de datos
    for registro in lista_registro:
        # Inserto las descripciones según el id_categoria
        valores = f'"{registro[0]}", {registro[1]}'
        query = f'INSERT INTO descripciones(detalle, valor, idcategoria) VALUES({valores}, {id_categoria})'
        cursor.execute(query)
        conexion.commit()
    conexion.close()

    # Redirijo al espacio de trabajo
    return redirect(url_for('interfaz_workspace'))

## Ruta para cerrar sesión

@app.route('/logout')
def cerrar_sesion():
    # Elimino los datos de sesión
    if "usuario" in session and "id_usuario" in session:
        session.pop("usuario")
        session.pop("id_usuario")
        return redirect(url_for('interfaz_logout_exitoso'))
    return redirect(url_for('interfaz_navegacion'))

@app.route('/editar_saldo', methods=['POST'])
def editar_saldo():
    # Si la sesión no está activa
    if not "usuario" in session:
        return redirect(url_for('interfaz_navegacion'))

    # Obtengo el nuevo saldo del formulario en tipo Float
    new_saldo = float(request.form.get("saldo"))
    # Obtengo el email del usuario
    email = session.get('usuario')
    # Creo la conexión a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    # Actualizo el saldo según el email del usuario
    query = f'UPDATE usuarios SET saldo={new_saldo} WHERE email="{email}"'
    cursor.execute(query)
    # Hago efectivos los cambios
    conexion.commit()
    # Cierro la conexión
    conexion.close()
    return redirect(url_for('interfaz_workspace'))

app.run(debug = True, port=5000)