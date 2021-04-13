#Cree un programa que tome el radio de un círculo e imprima su área y perímetro. Use funciones. Haga pruebas de escritorio.
radio = float(input("Ingrese el radio: "))
def circulo (radio):
    area = 3.14 * radio**2
    perimetro = 2 * 3.14 * radio
    return area, perimetro
area,perimetro = circulo(radio)
print("el area es: ", area,"el perimetro es: ",round(perimetro,1))  