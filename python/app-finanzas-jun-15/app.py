from flask import Flask, render_template, request, redirect, url_for, session

app = Flask("APP finanzas")

# cookie
### ESTA ES LA LLAVE QUE SE UTILIZA PARA ---> ENCRIPTAR Y DESEMCRIPTAR
app.secret_key = "a5jgrt8lodGGG55G7H8U5J11DED6SXCD"

# (BASES DE DATOS)
# 1--> Diccionario que guarda a los usuarios registrados 
usuarios = {}

# 2--> Diccionario que guarda las tarjetas creada (Fijos)

# [idtabla, idusuario, nombretabla] 
# [idregistro, idtabla, nombreproducto, costoproducto]
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

## Como hago yo para convertir las listas de arriba, en el diccionario de datos de abajo
# construir_datos(idusuario)

# 1
datos_tarjeta = {
    "Servicios" : {"Energia": 300, "Agua": 500},
    "Transporte" : {"Bus": 1000}
}

# 2
datos_tarjeta_2 = {
    "Inversiones": {"Bienes Raices": 2000}
}

### LISTA CON DICCIONARIO
# lista_tarjetas = [
#         {
#         "servicios":{"Energia":20.000,"Agua": 50.000,"Gas": 10.000,"Arrendo":60.0000},
#         "compras":{"Ropa":150.000,"Entretenimiento":100.000},
#         "transporte":{"Bus":20.000,"Uber":20.000,"Gasolina":60.000}
#         }        
#     ]

### FUNCIONES DE APOYO

def construir_datos(idusuario):
    datos = {}
    # Lista de tarjetas que pertenece al idusuario
    tarjetas_usuario = []
    # Convierto el idusuario para que entre como string
    idusuario = str(idusuario)    
    # Recorro las tarjetas
    for tarjeta in lista_tarjetas:
        # Obtengo el idusuario en los datos de la tarjeta
        id_usuario_tarjeta = tarjeta[1]
        if id_usuario_tarjeta == idusuario:
            # Agrego la tarjeta
            tarjetas_usuario.append(tarjeta)
    
    # Recorro cada tarjeta del usuario
    for tarjeta_usuario in tarjetas_usuario:
        # Obtengo el id de la tarjeta (A01, A02 etc)
        id_tarjeta = tarjeta_usuario[0]
        nombre_tarjeta = tarjeta_usuario[2]

        valores_tarjeta = []
        # Obtengo los valores de la tarjeta
        for elementos_items_tarjeta in lista_items_tarjeta:
            # Obtengo el id de la tabla a la que pertenece el valor
            id_valor_lista = elementos_items_tarjeta[1]
            # Si el id coincide con la tarjeta
            if id_valor_lista == id_tarjeta:
                # Lo agrego a la lista de valores
                valores_tarjeta.append(elementos_items_tarjeta)

        # Creo el diccionario de valores
        diccionario_valores = {}
        # Registro cada valor en el diccionario
        for valor in valores_tarjeta:
            # Obtengo los datos del valor
            nombre_valor = valor[2]
            costo_valor = valor[3]
            # Agrego los datos al diccionario
            diccionario_valores[nombre_valor] = costo_valor
        
        # Registro la tarjeta en los datos
        datos[nombre_tarjeta] = diccionario_valores

    print(datos)
    return datos

         
### ENRUTAGE
### render_template (MOSTRAR EN PANTALLA)
# Rutas unicamente para mostrar en pantalla

@app.route('/test')
def test():
    datos = construir_datos("1")
    return datos

@app.route('/')
def interfaz_navegacion():
    if "usuario" in session:
        return redirect(url_for('interfaz_workspace'))
    return render_template('navegacion.html', usuario=session.get('usuario'))

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
    tarjetas_usuario = construir_datos("1")
    return render_template('workspace.html', tarjetas = tarjetas_usuario, usuario=session.get('usuario'))

@app.route('/configuracion')
def interfaz_configuracion():
    return render_template('configuracion.html', usuario=session.get('usuario'))

@app.route('/editar_lista')
def interfaz_editar_lista():
    return render_template('editar-lista.html')

@app.route('/editar_saldo')
def interfaz_editar_saldo():
    return render_template('editar-saldo.html')

#--------------------------------------
# Esto es para cuando el login no es correcto
# Cuando el usuario ingresa un dato mal (usuario ó contraseña)
@app.route('/error_login')
def interfaz_login_incorrecto():
    return render_template('incorrecto_login.html')

# Ruta de cuando el usuario no esta registrado
@app.route('/usuario_no_registrado')
def interfaz_usuario_no_registrado():
    return render_template('usuario_no_registrado.html')

# Ruta donde se cierra sesion exitosamente
@app.route('/logout_exitoso')
def interfaz_logout_exitoso():
    return render_template('logout_exitoso.html')


#-----------------------------------------------------
### RUTAS

@app.route('/login', methods=['POST'])
def get_login():
    email = request.form.get("email")
    password = request.form.get("password")
    # Verifico que el email ingresado esta en la BD-->(usuarios)
    if usuarios.get(email):
        # Si el correo esta en la BD-->(usuarios)
        if usuarios[email]["password"] == password:
            # Si el usuario y contraseña coinciden con los de la BD
            # Se verifica la cookie
            # Se crea una sesion y se envia una cookie al navegador
            session["usuario"] = email
            #
            return redirect(url_for('interfaz_workspace'))
        return redirect(url_for('interfaz_login_incorrecto'))
    return redirect(url_for('interfaz_usuario_no_registrado'))
    

@app.route('/registro', methods=['POST'])
def get_registro():
    nombres = request.form.get("nombres")
    apellidos = request.form.get("apellidos")
    email = request.form.get("email")
    password = request.form.get("password")
    usuarios[email] = {"password":password, "nombres":nombres, "apellidos":apellidos}
    return redirect(url_for('interfaz_login'))


## Ruta para cerrar sesión
@app.route('/logout')
def cerrar_sesion():
    if "usuario" in session:
        session.pop("usuario")
        return redirect(url_for('interfaz_logout_exitoso'))
    return redirect(url_for("interfaz_usuario_no_registrado"))


@app.route('/editar_saldo')
def editar_saldo():
    return 'OK'

app.run(debug = True, port=5000)
