#Cree un programa que tome la base y la altura de un triángulo e imprima su área. Use funciones, incluya dos parámetros con valor por defecto. Haga pruebas de escritorio.

def triangulo (base = 10, altura =20):
    area = (base * altura) / 2
    return area
resultado = triangulo()
print(resultado)
