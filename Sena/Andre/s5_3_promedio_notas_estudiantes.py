#3. Cree un programa que calcule el promedio de tres notas para n estudiantes.
#  Use ciclo for. Use funciones. Haga pruebas de escritorio. 

def pedir_notas():
    lista = []
    for _ in range(3):
        lista.append(int(input("Cual es la nota: ")))
    return lista

def promedio_notas(lista):
    total = 0
    for i in lista:
        total = total + i
    return round(total / 3)

lista_notas = pedir_notas()
promedio = promedio_notas(lista_notas)
print(f"El promedio de sus notas es: {promedio}")
    




