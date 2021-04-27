''' 
programa que almacene los documentos y nombres de diez usuarios, donde a cada documento
corresponda su respectivo nombre. Use diccionarios. Imprima todos los nombres de los usuarios usando el ciclo
for.
'''
Nombres = {}
print ("----------------------------------------")
for i in range(4):
	dato = int(input("Ingrese el Documento: \n"))
	dato1= str(input("Ingrese el Nombre: \n"))
	Nombres[dato]=dato1
	print (Nombres)	## se va mostrando el cresimiento y los datos del Diccionario
#print ("----------------------------------------\n")
print("los nombres ingresados son:")
for i in Nombres:
	print (Nombres[i])
print ("----------------------------------------\n")