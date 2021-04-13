# Cree un programa que pida al usuario la fecha 
# de su nacimiento, almacene tal valor en una 
# constante e imprima un mensaje al usuario 
# notificando el día de su cumpleaños

# Algoritmo cumpleaños

#     cadena dia = "Ingrese el dia de nacimiento: "
#     leer(dia)
#     cadena mes = "Ingrese el mes de nacimiento: "
#     leer(mes)
#     cadena año = "Ingrese año de nacimiento: "
#     leer(año) 
#     cadena fecha_nacimiento = dia + mes
   
#     imprimir = fecha_nacimiento

# FinAlgoritmo
print("por favor ingrese su fecha de nacimiento: Dia, Mes y Año")
dia = input("Ingrese el dia de nacimiento: ")
mes = input("Ingrese el mes de nacimiento: ")
año = input("Ingrese año de nacimiento: ")

fecha_nacimiento = dia + " de " + mes
print("su cumpleaños es el:",fecha_nacimiento)