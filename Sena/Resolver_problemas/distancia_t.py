#Realice un programa que calcule la distancia entre dos puntos en el espacio tridimensional.
import math # aqui importo la libreria matematicas
x1 = float(input("ingrese valor de x1:"))
y1 = float(input("ingrese valor de y1:"))
z1 = float(input("ingrese valor de z1:"))

x2 = float(input("ingrese valor de x2:"))
y2 = float(input("ingrese valor de y2:"))
z2 = float(input("ingrese valor de z2:"))

#formula:
# raiz((x2-x1)**2 + (y2 -y1)**2 + (z2 - z1)**2)

distancia = math.sqrt((x2-x1)**2 + (y2 -y1)**2 + (z2 - z1)**2)
print(distancia)

