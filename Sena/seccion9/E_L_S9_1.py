''' 
Programa que usa una función de un parámetro, a la cual se le pase como argumento un arreglo, de
tal manera que la función retorne la longitud(número de elementos) del arreglo.
'''
##############################################################
vector = [1,2,3,4,5,6,7,8,9,0]
def  fun(c):
	a=len(c)
	return (a)
 

fun(vector)
longitud=fun(vector)
print ("El vector es:", vector)
print("La longitud del vector es",longitud)
