''' 
Dado los siguientes arreglos arreglo1 = [ [“A”, “B”, “C”], [“D”, “E”, “F”], [“G”, “H”, “I”] ] y 
arreglo2 = [ [“J”, “K”, “L”],[“M”, “N”, “O”], [“P”, “Q”, “R”] ] ,
use ciclos para intercambiar los elementos de los arreglos.
'''
##############################################################
from copy import copy, deepcopy
Auxi=[]
Arreglo1 = [["A","B", "C"], ["D", "E", "F"], ["G", "H", "I"]] 
Arreglo2 = [["J", "K", "L"],["M", "N", "O"], ["P", "Q", "R"]]
print ("Datos Arreglo 1 Y 2")
print (Arreglo1)
print (Arreglo2)
Auxi=deepcopy(Arreglo1)
#Auxi=Arreglo1
print("_________________________________________")
tama=len(Arreglo1)
for i in range(tama):
	for j in range(tama):
		Arreglo1[i][j]=Arreglo2[i][j]
		Arreglo2[i][j]=Auxi[i][j]
print ("Id de los arreglos")
print("_________________________________________")
print ("La id de AR1 =", id(Arreglo1), "->", Arreglo1)
print ("La id de AR2 =", id(Arreglo2), "->", Arreglo2)
print ("La id de Aux =", id(Auxi), "->", Auxi)
print("_________________________________________")
print ("Datos Arreglos intercambiados")
print(Arreglo1)
print(Arreglo2)



