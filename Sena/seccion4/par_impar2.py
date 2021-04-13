#Cree un programa que lea un número y muestre si este es par o impar. Use funciones. Haga pruebas de escritorio.

#Problema:
#numero % 2 == 0 es par
#numero % 2 != 0 es impar
#numero = caracter o float es Error, ingrese solo numeros enteros

#datos:
#numero

#solucion:
try: 
    numero_entrada = int(input("Ingrese un numero, por favor: ")) #evita erroes (tratar de convertir caracteres o decimales en enteros)
except:
    print("Ingrese solo numeros enteros")    
    exit()

def consultar_numero (numero):
    if numero % 2 == 0:
        print("Es par")
    else: 
        print("Es impar")  

consultar_numero(numero_entrada)


