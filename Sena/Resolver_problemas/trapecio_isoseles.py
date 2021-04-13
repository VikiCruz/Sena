# 2.Realice un programa que calcule el área de un trapecio isósceles.

base_menor = float(input("Ingrese la base menor: "))
base_mayor =float(input("Ingrese la base mayor: "))
altura = float(input("Ingrese la altura: "))
area = ((base_mayor + base_menor)/2 ) * altura
print("El area del trapecio es: ", str(area))