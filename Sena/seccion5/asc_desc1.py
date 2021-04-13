#Cree un programa que imprima los números enteros entre 0 y 100 en orden ascendente y descendente. Use ciclo for. Use funciones. Haga pruebas de escritorio.
# problema:

# datos:

#solucion:
numero_max = 100
def numero_ascendente(numero, ascendente = True):
    if ascendente == True:
        print("Números del 0 al 100 en orden ascendente")
    else:
        print("Números del 0 al 100 en orden descendente")   
    for i in range(0, numero + 1): #para i en el rango (0, número + 1)
        if ascendente: 
            print(i)
        else:
            print(numero-i)

numero_ascendente(numero_max)
numero_ascendente(numero_max, False)