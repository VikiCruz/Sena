# Cree un programa que lea la edad de un usuario y muestre 
# cuántos años tendrá el usuario dentro
# de tantos años como este indique. 
# Por ejemplo, si el usuario 
# tiene 20 años y quiere saber cuántos años tendrá dentro de 15 
# años, el programa deberá mostrar que tendrá 35 años.

# Algoritmo años proximos

#     entero edad_actual,edad_anos,edad_prox
#     imprimir("Ingrese su edad")
#     leer(edad_actual)
#     imprimir("Ingrese los años a futuro")
#     leer (edad_anos)

#     edad_prox= edad_actual + edad_anos
#     imprimir(edad_Prox)

# FinAlgoritmo

edad_actual =int(input("Ingrese cuantos años tiene: "))
edad_anos = int(input("ingrese años a futuro: "))
edad_prox = edad_actual + edad_anos

print("su edad en " + str(edad_anos) + " años es de:",str(edad_prox) + " años")