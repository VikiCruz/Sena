#Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden a un triángulo o no. Use funciones. Haga pruebas de escritorio.

#Problema:
# entra al try y si encuentra un error como un caracter en angulo1, angulo2, angulo3 lo trata de convertir en float generando un mensaje:El valor ingresado debe ser natural o decimal, evitando de esta manera mostrar un error al usuario
#triangulo = angulo1 + angulo2 + angulo3
#Si a1 es menor que 0 o a2 es menor que 0 o a3 es menor que 0 = ERROR, el valor ingresado no puede ser negativo
#Si triangulo es igual a 180 Es un triangulo
#Si triangulo es dieferente a 180 Es un triangulo

#datos:
#angulo1, angulo2, angulo3

#solucion:
print("________________________________________________________________________________________________________________________\n")
print("Hola, el siguiente programa te mostrara si los angulos ingresados por ti corresponde a un tríangulo o no\n")
try: #evita erroes (tratar de convertir caracteres en FLOAT)
    angulo1 = float(input("Por favor ingresa el primer ángulo del tríangulo: "))
    angulo2 = float(input("Por favor ingresa el segundo ángulo del tríangulo: "))
    angulo3 = float(input("Por favor ingresa el tercero ángulo del tríangulo: "))   
except:
    print("El valor ingresado debe ser natural o decimal\n ")    
    exit()

def calcular_triangulo(a1, a2, a3):
    triangulo = a1 + a2 + a3
    if a1 < 0 or a2 <0 or a3 < 0:
        return print("ERROR, el valor ingresado no puede ser negativo\n")    
    if triangulo == 180:
        return print ("Es un triangulo\n")
    if triangulo != 180:   
        return print("No es un triangulo\n")

calcular_triangulo(angulo1, angulo2, angulo3)

#Los números naturales pertenecen al conjunto de los números enteros positivos: no tienen decimales, no son fraccionarios y se encuentran a la derecha del cero en la recta real. Son infinitos, ya que incluyen a todos los elementos de una sucesión (1, 2, 3, 4, 5…).   

#Los números reales incluyen a los números naturales o números contables, números enteros positivos, números enteros, números racionales, y números irracionales. El conjunto de los números reales contiene a todos los números que tienen un lugar en la recta numérica.