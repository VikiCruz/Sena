 
''' Dado el siguiente arreglo [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]:
 ● Iterar por todos los elementos del arreglo utilizando while y mostrarlos en pantalla.
 ● Iterar por todos los elementos del arreglo utilizando el ciclo “for” y mostrarlos en pantalla.
 ● Crear otro arreglo que sea idéntico al arreglo dado, pero con todos los elementos incrementados en 1.
 Para esto debe usar ciclo for y a través de iteraciones ir formando el nuevo arreglo con sus elementos tal
 cual se piden.
 ● Usando el ciclo “for” Calcular el promedio de todos los elementos del arreglo
 '''
def mostrar(j):
	i=0
	while (i<3):
		print ("en la posicion",j,",",i,":",Dato[j][i])
		i=i+1
##############################################################
i=0
con=0
Dato = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
copia_dato = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
suma=0
print ("Datos en el arreglo usando 'while'")
mostrar(con)
con=con+1
mostrar(con)
con=con+1
mostrar(con)
print ("--------------------------------------------\n")
print ("Datos en el arreglo usando 'for'")
for i in range(len(Dato)):
    for j in range(len(Dato[i])):
        print(Dato[i][j], end=' ')
    print()
print ("--------------------------------------------\n")
print ("Datos en el arreglo usando 'for'+1 en cada valor")
for i in range(len(Dato)):
    for j in range(len(Dato[i])):
    	copia_dato[i][j]=Dato[i][j]+1
    	print(copia_dato[i][j], end=' ')
    print()
for i in range(len(Dato)):
    for j in range(len(Dato[i])):
    	suma=Dato[i][j]+suma
promedio= suma/9
print ("El proedio de los datos es :",promedio)