''' 
Función que permita encontrar el número menor contenido en una matriz recibida como
parámetro.
'''
##############################################################
Vector= []
suma=0
def calculo(uno):
	suma=0
	num=len(uno)
	for i in range(num):
		suma=suma+(uno[i]*uno[i])
	return suma


n_datos = int(input("Ingrese el numero de datos: \n"))
for i in range(n_datos):
	dat = int(input('Ingrese dato (%d):'%(i)))
	Vector.append(dat)
print (Vector)
sumas=calculo(Vector)
print("la suma de los cuadrados del los",n_datos,"elemntos es:",sumas)