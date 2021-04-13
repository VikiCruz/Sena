#2. Cree un programa que imprima la tabla de multiplicar del 3,
# del 0 al 50. Use ciclo for. Use funciones. Haga pruebas de escritorio. 
numero_max = 50
def tabla_del_tres(numero):
    for i in range(0,numero + 1):
        resultado_tabla = i * 3
        print(f" 3 x {i} = {resultado_tabla}")
tabla_del_tres(numero_max)
