'''
Cree un programa que solicite al usuario el nombre de uno de los cinco continentes, luego muestre cinco paises del continente seleccionado
por el usuario. Use diccionarios. Use ciclo for
'''
Continentes = {'America':['Canada','Estados Unidos','Mexico','Colombia','Brasil'],'Asia':['China','Corea del Norte','Corea del sur','India','Japón'],'Africa':['Congo','Sudafrica','Camerun','Egipto','Tunez'], 'Europa':['Alemania','España','Francia','Inglaterra','Escocia'], 'Oceania':['Australia','Islas Mauricio','Nueva Zelanda','Islas Solomon','Islas Fiji']}
conti = str(input("Ingrese el Continete: \n"))

print ("----------------------------------------")
print ("Paises del contiente",conti)
for i in range(5):
	print (Continentes[conti][i])
print ("----------------------------------------\n")