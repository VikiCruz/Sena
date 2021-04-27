 
''' 
1. Dado la siguiente lista = [1,2,3,4,5,6,7,8,9,10];
a) Usando ciclo for recorra la lista imprimiendo cada uno de sus elementos.
b) Usando ciclo while recorra la lista imprimiendo cada uno de sus elementos.
c) Usando ciclo for recorra la lista imprimiendo cada uno de sus elementos aumentados en 3.
d) Usando ciclo while recorra la lista imprimiendo cada uno de sus elementos aumentados en 3.
e) Usando ciclo for recorra la lista imprimiendo únicamente los números impares.
f) Usando ciclo while recorra la lista imprimiendo únicamente los números pares.
 '''

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copia_Lista=[0,0,0,0,0,0,0,0,0,0]
aumento=3

print ("--------------------------------------------\n")
print ("Datos en el arreglo usando 'for'")
print(Lista)
for i in range(len(Lista)):
    print("Dato",i,"de la lista: ",Lista[i])
print ("--------------------------------------------\n")
print ("Datos en el arreglo usando 'While'")
i=0
while (i<len(Lista)):
    print ("En la posicion",i,"El dato es:",Lista[i])
    i=i+1
print ("--------------------------------------------\n")
i=0
print ("Datos en el arreglo usando 'for' + 3")
for i in range(len(Lista)):
    copia_Lista[i]=Lista[i]+3
    print("Dato",i,"de la lista aumentada en 3: ",copia_Lista[i])
print ("--------------------------------------------\n")
i=0
print ("Datos en el arreglo usando 'While' + 3")
while (i<len(Lista)):
    print ("En la posicion",i,"El dato aumentado en 3 es:",copia_Lista[i])
    i=i+1
print ("--------------------------------------------\n")
print ("Datos impares en el arreglo usando 'for'")
print (Lista)
i=0
for i in range(0,len(Lista),2):
    print("Dato",i,"de la lista: ",Lista[i])
print ("--------------------------------------------\n")
i=0
print ("Datos pares en el arreglo usando 'While'")
print (Lista)
while (i<len(Lista)):
    if ((Lista[i]%2)==0):
        print ("En la posicion",i,"El dato par es:",Lista[i])
    i=i+1