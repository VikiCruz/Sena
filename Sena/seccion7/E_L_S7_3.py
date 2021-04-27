 
## Dado el arreglo [1,2,3,4,5,6]
## ● Iterar por todos los elementos dentro del arreglo utilizando while y mostrarlos en pantalla.
## ● Iterar por todos los elementos dentro del arreglo utilizando el ciclo “for” y mostrarlos en pantalla.
## ● Mostrar todos los elementos dentro del arreglo sumándole uno a cada uno.
## ● Crear una copia del arreglo usando el ciclo “for” pero con todos los elementos incrementados en 1.
## ● Calcular el promedio de todos los elementos del arreglo

##############################################################
suma=0
i=0
Dato = [1,2,3,4,5,6]
copia_dato = [0,0,0,0,0,0]
print ("Datos en el arreglo usando while")
k=len(Dato)
while (i<k):
	print ("en la posicion",i,":",Dato[i])
	i=i+1
print ("--------------------------------------------------\n")	
print ("Datos en el arreglo usando for")
for i in range(k):
	print ("en la posicion",i,":",Dato[i])
print ("--------------------------------------------------\n")
print ("Datos en el arreglo + 1 a cada dato")
for i in range(k):
	print ("en la posicion",i,":",Dato[i]+1)
print ("--------------------------------------------------\n")
print ("Copia de arreglo con datos incrementados en 1")
for i in range(k):
	copia_dato[i]=Dato[i]+1
print (copia_dato)
for i in range(k):
	suma=suma+Dato[i]
promedio=suma/k
print ("El proedio de los datos es :",promedio)
