import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#credenciales
proveedor_correo = 'smtp.live.com: 587'
remitente = 'correoempresa'
password = 'clave'
#conexion a servidor
servidor = smtplib.SMTP(proveedor_correo)
servidor.starttls()
servidor.ehlo()
#autenticacion
servidor.login(remitente, password)
#mensaje 
mensaje = "<h1>Producto 1</h1> <h1>Producto 2</h1>"
msg = MIMEMultipart()
msg.attach(MIMEText(mensaje, 'html'))
msg['From'] = remitente
msg['To'] = 'gangaritah@gmail.com'
msg['Subject'] = 'Prueba cliente correo ADSI RAPPI'
servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
