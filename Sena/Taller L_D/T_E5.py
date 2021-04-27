'''. Dado el siguiente arreglo [1, 2, 3, 4, 500, 420, -100] elimine el elemento de índice 4 y a continuación,
elimine el último elemento de la lista usando el método pop(si al método pop no se le pasa argumento,
eliminará el último elemento de la lista) el cual puede consultar aquí:
https://www.geeksforgeeks.org/python-list-pop/ . Agregue el elemento 520 usando el método append.
Finalmente, haga una copia “independiente del arreglo” usando el método copy el cual puede consultar
acá: https://www.programiz.com/python-programming/methods/list/copy'''
from copy import copy, deepcopy

print("lista original")
lista = [1, 2, 3, 4, 500, 420, -100]
print (lista)
print("borra el elemento 5 con el valor 500 y el indice 4, muestra como quedaria la lista")
print(lista.pop(4), lista)
print("------------------------------------\n")
print("borra el ultimo elemento  y muestra como quedaria la lista")
print(lista.pop(), lista)
print("agregamos a la lista el elemento con el valor 520")
lista.append(520)
print(lista)
print("------------------------------------\n")
print("se genera la copia en diferente posicion en memoria - lista es la original")
lista_copia = deepcopy(lista) # se genera una copia profunda de lista
print("a la copia se le añade un elemento - lista_copia es la copia con el nuevo elemento en diferente posicion en memoria")
lista_copia.append("ARQSOFT")
print(lista_copia)
print ("La id de lista =", id(lista), "->", lista)
print ("La id de lista_copia =", id(lista_copia), "->", lista_copia)