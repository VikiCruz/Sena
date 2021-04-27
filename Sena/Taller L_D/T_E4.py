'''Dada la siguiente cadena “Programar es algo genial, todos deberían intentarlo, atrévete!” genere el
siguiente arreglo [“Programar es algo genial”, “todos deberían intentarlo”, “atrévete!”] usando el método
split el cual puede consultar en el siguiente link:
https://blog.carreralinux.com.ar/2017/07/uso-split-y-join-python/..'''

# SPLIT convierte una cadena a una lista separadas por un caracter deseado

mensaje = "Programar es algo genial, todos deberían intentarlo, atrévete!"

mensaje_split = mensaje.split(",")
print(mensaje_split)

#['Programar es algo genial', ' todos deberían intentarlo', ' atrévete!']