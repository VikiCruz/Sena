#Cree un programa que tome el precio de un producto e imprima su precio final al consumidor con un IVA de 19%. Use funciones, incluya por lo menos un parámetro con valor por defecto. Haga pruebas de escritorio.

#Problema:
#precio final = precio * IVA

#datos:
#precio,IVA

#solucion:

def precio_final (precio, IVA = 1.19):
    resultado = precio * IVA 
    return resultado

precio = float(input("Ingrese un precio : "))
if precio < 0:
    print("No ingrese valores negativos")
    exit()

precio_iva = precio_final(precio)
print ("el valor del producto con IVA es: ",precio_iva)

