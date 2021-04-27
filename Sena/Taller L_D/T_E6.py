# En una empresa se requiere un sistema de información que registre sus nuevos usuarios. 
# Cada vez que un usuario se registra debe introducir los siguientes datos: 
# documento, nombres, apellidos, edad, peso, estatura. 
# Cree un sistema de información que reciba los datos de registro de cada cliente por 
# teclado, luego de realizado el registro el sistema debe mostrar al usuario el mensaje 
# “Registro exitoso”. Si el usuario desea consultar su registro 
# debe poder hacerlo a través de su documento

def agregar():
    usuarios = {}
    nuevo_usuario="s"
    while nuevo_usuario=="s" or nuevo_usuario=="S":
        documento=int(input("Ingrese el documento: "))
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        edad=input("Ingrese su edad en años: ")
        peso=input("Ingrese su peso en kilos: ")
        usuarios[documento]=(nombre,apellido,edad,peso)
        nuevo_usuario=nuevo_usuario=input("Desea agregar otro usuario[s/n]? ")
    print("**** REGISTRO EXITOSO ***** \n")
       
    return usuarios


def imprimir(usuarios):
    print("Usuarios Registrados en el Sistema")
    for documento in usuarios:
       print("Documento:",documento,"- " "Nombres:",usuarios[documento][0], "- Apellidos:" ,usuarios[documento][1],"- Edad:",usuarios[documento][2], "- Años", "- Peso:", usuarios[documento][3], "- Kilos") 


def consulta(usuarios):
    documento=int(input("Ingrese el documento del usuario a consultar: "))
    if documento in usuarios:
         print("Los datos del usuario con el documento:",documento,"- Nombres:",usuarios[documento][0], "- Apellidos:" ,usuarios[documento][1],"- Edad:",usuarios[documento][2], "- años","- Peso:", usuarios[documento][3], "- Kilos") 
    else:
        print("**** Documento no encontrado ***")            
usuarios=agregar()
imprimir(usuarios)
consulta(usuarios)
