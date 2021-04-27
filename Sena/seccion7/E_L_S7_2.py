 
## un programa que implemente un arreglo de 10 elementos(los dígitos), ordenados de menor
## a mayor e imprima cada uno de ellos en el mismo orden en el que se encuentran en el arreglo. Luego, invierta el
## orden de todos los elementos del arreglo, haciendo que el último pase a ser el primero, el penúltimo pase a ser el
## segundo, así sucesivamente, e imprima nuevamente cada elemento en el mismo orden en el que ahora se
## encuentran en el arreglo.

def mostrar(j):
	k=len(j)
	for i in range(k):
		print ("en la posicion",i,":",j[i])
	print ("--------------------------------------------------\n")

##############################################################

Dato = [8, 4, 6, 1, 7, 9, 5, 3, 0, 2]
print ("Datos en el arreglo inicial")
mostrar(Dato)
Dato.reverse()
print ("Datos Invertidos")
mostrar(Dato)