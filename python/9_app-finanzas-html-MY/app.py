from flask import Flask, render_template, request, redirect, url_for, session

app = Flask("APP finanzas")

# cookie
### ESTA ES LA LLAVE QUE SE UTILIZA PARA ---> ENCRIPTAR Y DESEMCRIPTAR
app.secret_key = "a5jgrt8lodGGG55G7H8U5J11DED6SXCD"

# Diccionario que guarda a los usuarios registrados 
# (BASE DE DATOS)
usuarios = {}


### ENRUTAGE
### render_template (MOSTRAR EN PANTALLA)
# Rutas unicamente para mostrar en pantalla
@app.route('/')
def interfaz_navegacion():
    return render_template('navegacion.html')

@app.route('/login')
def interfaz_login():
    return render_template('login.html')

@app.route('/registro')
def interfaz_registro():
    return render_template('registro.html')

@app.route('/workspace')
def interfaz_workspace():
    return render_template('workspace.html')

@app.route('/configuracion')
def interfaz_configuracion():
    return render_template('configuracion.html')

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

@app.route('/tarjetas')
def datos_tarjetas():
    lista_tarjetas = [
            {
            "servicios":{"Energia":20.000,"Agua": 50.000,"Gas": 10.000,"Arrendo":60.0000},
            "Compras":{"Ropa":150.000,"Entretenimiento":100.000},
            "Transporte":{"Bus":20.000,"Uber":20.000,"Gasolina":60.000}
            }
        ]
    return render_tamplate(interfaz_workspace, informacion_tarjetas=lista_tarjetas))

app.run(debug = True, port=5000)