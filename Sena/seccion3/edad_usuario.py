#Cree un programa que lea la edad de un usuario e imprima un mensaje que diga si el usuario es mayor de edad o no. Use funciones. Haga pruebas de escritorio.

#Problema:
#edad > 18 = "es mayor de edad"
#edad < 18 = "es menor de edad"

#datos:
#edad

#solucion:

def evaluar_edad_usuario(edad, limite_edad):
    if edad >= limite_edad:
        print("Es mayor de edad")
    else: 
        print("Es menor de edad")    

entrada_edad = int(input("Ingrese su edad:"))
edad_max = int(input("Ingrese el limite mayor de edad: "))

if entrada_edad < 0 :
    print("No ingrese datos negativos")
    exit()

evaluar_edad_usuario(entrada_edad, edad_max)
