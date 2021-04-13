#4.	Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no. Use funciones. Haga pruebas de escritorio.

# un número primo:
# Es un número natural
# Es mayor que 1
# Son divisibles por sí mismo y por 1

#Problema:


#datos:
#numero

#solucion:
print("________________________________________________________________________________________________________________________\n")
print("Hola, el siguiente programa te verificara si el numero que ingresas entre 1 y 15 es primo o no\n")

numeros_primos = [2,3,5,7,11,13]
try:  #evita erroes (tratar de convertir caracteres o decimales en enteros)
    numero_entrada = int(input("Ingresa un número entre 1 y 15: "))
except: 
    print("El numero ingresado debe ser natural")
    exit()

def verificar_rango_numero(numero):
    if numero < 0:
        print("Número no valido, no se permiten numero negativos")
        exit()

    if numero < 1 or numero >= 16:
        print("Número no valido, ingresa numeros entre 1 y 15")
        exit()

def validar_numero_primo(numero):
    if numero in numeros_primos:
        print("El número es primo")
    else:
        print("El número no es número primo")


verificar_rango_numero(numero_entrada)
validar_numero_primo(numero_entrada)
