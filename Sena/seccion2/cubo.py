#Cree un programa que tome el lado de un cubo e imprima su volumen. Use funciones, incluya un parámetro con valor por defecto. Haga pruebas de escritorio
#Problema:
#volumen= lado**3
#datos:
#volumen, lado
#solucion:

def cubo(lado = 0):
    volumen = lado **3
    return volumen

entrada = float(input("Ingrese el lado : "))

if entrada < 0:
    print(f"error: no se puede operar con el lado negativo > {entrada}")
    exit()
resultado = cubo(entrada)
print(resultado)

