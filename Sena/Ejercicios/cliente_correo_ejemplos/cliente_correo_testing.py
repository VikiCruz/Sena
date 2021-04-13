import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from credenciales import remitente, password
from datetime import date

#credenciales
proveedor_correo = 'smtp.live.com: 587'
nombre = input("Ingrese el nombre del cliente:")
correo = input("Ingrese un correo por favor:")
fecha = date.today()

vestido = 35000
pantaloneta = 25000
chaqueta = 80000
blusa = 20000
jeans = 50000
IVA = 1.19

def mostrar_productos():
    print("lista de productos:")
    print("0: vestido = 35000") 
    print("1: pantaloneta = 25000")
    print("2: chaqueta = 80000")
    print("3: blusa = 20000")
    print("4: jeans = 50000")

def decision_p(nombre):
    decision = input(f"desear comprar {nombre}? s/n: ") == "s"
    return decision

def elegir_productos():
    elecciones = []
    elecciones.append(decision_p("vestido"))
    elecciones.append(decision_p("pantaloneta"))
    elecciones.append(decision_p("chaqueta"))
    elecciones.append(decision_p("blusa"))
    elecciones.append(decision_p("jeans"))
    return elecciones

def calcular_precio_IVA (precio):
    precio_IVA = precio * IVA
    return precio_IVA 

mostrar_productos()

elecciones = elegir_productos()

mensaje_productos = ""
if elecciones [0]:
    mensaje_productos += f"<h2>vestido</h2>"

IVA_vestido = calcular_precio_IVA(blusa)
IVA_pantaloneta = calcular_precio_IVA(pantaloneta)
IVA_chaqueta = calcular_precio_IVA(chaqueta)
IVA_blusa = calcular_precio_IVA(blusa)
IVA_jeans = calcular_precio_IVA(jeans)

#conexion a servidor
servidor = smtplib.SMTP(proveedor_correo)
servidor.starttls()
servidor.ehlo()
#autenticacion
servidor.login(remitente, password)
#mensaje 
mensaje = f"<h1>Emitada por ADSITOP, para: {nombre}</h1> <h2>fecha: {fecha}</h2>"
msg = MIMEMultipart()
msg.attach(MIMEText(mensaje, 'html'))
msg['From'] = remitente
msg['To'] = 'bikiliseth2237@gmail.com'
msg['Subject'] = 'Factura de electronica ADSITOP'
servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
