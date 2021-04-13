#Cree un programa que lea un número y muestre si este es divisible entre cinco o no. Use funciones. Haga pruebas de escritorio.

#Problema:
# entra al try y si encuentra un error como un caracter  en numero_entrada lo trata de convertir en decimal generando un mensaje:Ingrese solo numeros enteros, evitando de esta manera mostrar un error al usuario
#numero_entrada % 5 == 0 Es divisible entre 5
#numero_entrada % 5 != 0 No es divisible entre 5


#datos:
#numero_entrada

#solucion:

try: 
    numero_entrada = float(input("Ingrese un numero, por favor: ")) #evita erroes (tratar de convertir caracteres en decimales )
except:
    print("ERROR,Ingrese solo numeros enteros")    
    exit()

def consultar_numero (numero):
    if numero % 5 == 0:
        print("Es divisible entre 5")
    else: 
        print("No es divisible entre 5")  

consultar_numero(numero_entrada)

