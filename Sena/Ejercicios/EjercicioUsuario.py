# Cree un programa que pida al usuario su edad, 
# domicilio y estado civil, a continuación, 
# confirme al usuario los valores introducidos 
# por éste

# Algoritmo usuario

#     Entero edad = "Ingrese su edad"
#     leer (edad)
#     caracter domicilio = "Ingrese su direccion de residencia"
#     leer (domicilio)
#     caracter estado_civil ="Ingrese su estado civil: soltero, casado, divorciado, union libre, viudo"
#     leer (estado_civil)

#     imprimir ("su edad es:")
#     imprimir (edad)
#     imprimir ("su direccion de residencia es:")
#     imprimir (domicilio)
#     imprimir ("estado civil es:)
#     imprimir (estado_civil)

# FinAlgoritmo

edad = input("Ingrese su edad: ")
domicilio = input("Ingrese su direccion de residencia: ")
estado_civil = input ("Ingrese su estado civil: \nSoltero  \ncasado \ndivorciado \nunion libre \nviudo \n:")

print("su edad es:",edad + " años")
print("su direccion de residencia es:",domicilio)
print("estado civil es:",estado_civil)
