#1. El sistema tiene correo de la empresa para enviar facturas
import smtplib
#import credenciales
from credenciales import USER, PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


nombre_cliente = input("Cual es su nombre: ")
fecha = datetime.datetime.now()
correo_electronico = input("Cuál es su correo electronico: ")

print("Elija los productos a comprar: ")
print("Blusa: $20.000")
print("Pantalon: $50.000")
print("Vestido: $60.000")
print("Falda: $40.000")
print("Kimono: $80.000")


cant_blusa = int(input("Cuantos blusas vas a comprar: "))
cant_pantalon = int(input("Cuantos pantalones vas a comprar: "))
cant_vestido = int(input("Cuantos vestidos vas a comprar: "))
cant_faldas = int(input("Cuantos faldas vas a comprar: "))
cant_kimonos = int(input("Cuantos kimonos vas a comprar: "))

#Definir variables
blusa = 20000
pantalon = 50000
vestido = 60000
falda = 40000
kimono =80000
IVA = 0.19

def calcular_precio_cant (precio, cantidad):
    precio_cant = (precio * cantidad)
    return precio_cant

def calcular_precio_IVA (precio, cantidad):
    precio_IVA = (precio * cantidad) * IVA
    return precio_IVA
    
def calcular_valor_total(producto, valor_IVA):
    valor_total = producto + valor_IVA
    return valor_total    


precio_cant_blusa = calcular_precio_cant(blusa, cant_blusa)
precio_cant_pantalon = calcular_precio_cant(pantalon, cant_pantalon)
precio_cant_vestido = calcular_precio_cant(vestido, cant_vestido)
precio_cant_falda = calcular_precio_cant(falda, cant_faldas)
precio_cant_kimono = calcular_precio_cant(kimono, cant_kimonos)


IVA_blusa = calcular_precio_IVA(blusa, cant_blusa)
IVA_pantalon = calcular_precio_IVA(pantalon, cant_pantalon)
IVA_vestido = calcular_precio_IVA(vestido, cant_vestido)
IVA_falda = calcular_precio_IVA(falda, cant_faldas)
IVA_kimono = calcular_precio_IVA(kimono, cant_kimonos)

valor_total_blusa = calcular_valor_total(precio_cant_blusa, IVA_blusa)
valor_total_pantalon = calcular_valor_total(precio_cant_pantalon, IVA_pantalon)
valor_total_vestido = calcular_valor_total(precio_cant_vestido, IVA_vestido)
valor_total_falda = calcular_valor_total(precio_cant_falda, IVA_falda)
valor_total_kimono = calcular_valor_total(precio_cant_kimono, IVA_kimono)

total_bruto = precio_cant_blusa + precio_cant_pantalon + precio_cant_vestido + precio_cant_falda + precio_cant_kimono
suma_iva = IVA_blusa + IVA_pantalon + IVA_vestido + IVA_falda + IVA_kimono
valor_pagar = total_bruto + suma_iva

#importar archivo html
f = open("index.html", "r")
factura_html = f.read().format(
    nombre_cliente=nombre_cliente,
    correo_electronico=correo_electronico,
    fecha=fecha,
    blusa=blusa,
    pantalon=pantalon,
    vestido=vestido,
    falda=falda,
    kimono=kimono,
    total_bruto=total_bruto,
    precio_cant_blusa=precio_cant_blusa,
    precio_cant_pantalon=precio_cant_pantalon,
    precio_cant_vestido=precio_cant_vestido,
    precio_cant_falda=precio_cant_falda,
    precio_cant_kimono=precio_cant_kimono,
    cant_blusa=cant_blusa,
    cant_pantalon=cant_pantalon,
    cant_vestido=cant_vestido,
    cant_faldas=cant_faldas,
    cant_kimonos=cant_kimonos,
    IVA_blusa=IVA_blusa,
    IVA_pantalon=IVA_pantalon,
    IVA_vestido=IVA_vestido,
    IVA_falda=IVA_falda,
    IVA_kimono=IVA_kimono,
    valor_total_blusa=valor_total_blusa,
    valor_total_pantalon= valor_total_pantalon,
    valor_total_vestido= valor_total_vestido,
    valor_total_falda=valor_total_falda,
    valor_total_kimono=valor_total_kimono,
    suma_iva=suma_iva,
    valor_pagar=valor_pagar
    )

#Enviar correo   
#credenciales
proveedor_correo = 'smtp.live.com: 587'
remitente = USER
password = PASSWORD
#conexion a servidor
servidor = smtplib.SMTP(proveedor_correo)
servidor.starttls()
servidor.ehlo()
#autenticacion
servidor.login(remitente, password)

#mensaje 
mensaje = "<h1>Producto 1</h1> <h1>Producto 2</h1>"
msg = MIMEMultipart()
msg.attach(MIMEText(factura_html, 'html'))
msg['From'] = remitente
msg['To'] = correo_electronico
msg['Subject'] = 'Factura electronica'
servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

