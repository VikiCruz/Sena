''' 
Función que permita encontrar el número menor contenido en una matriz recibida como
parámetro.
'''
##############################################################
matriz = []
def vet_matriz(f,c):
	i=-1
	j=-1
	v_fil = []
	a = []
	for i in range(f):
		v_col=[]
		i=i+1
		for j in range(c):
			dat = int(input('Ingrese dato (%d,%d):'%(i,j)))
			v_col.append(dat)
		v_fil.append(v_col)
	matriz=v_fil
	val=len(matriz)
	a=matriz
	for i in range(val):
		matriz[i].sort()
		a[i]=matriz[i][0]
	a.sort()
	print("el nimimo valor :",a[0])
 

filas = int(input("Ingrese el numero de filas: \n"))
columnas = int(input("Ingrese el numero de columna: \n"))
l=vet_matriz(filas,columnas)