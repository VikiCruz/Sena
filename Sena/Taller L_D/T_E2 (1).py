''' 
persona = {“edad”: 20, “peso”: 75, “nombres”: “Pedro”, “apellidos”: "Pérez
Pérez"};

Usando ciclo for y el método keys(), imprima todas las claves del diccionario dado, también, usando ciclo
for y el método values() imprima todos los valores del diccionario. Luego, sobre el mismo diccionario
realice las siguientes operaciones:
● Cambie el valor de la clave peso por 77
● Cambie el valor de la clave edad por 21
● Elimine la clave apellidos usando método pop
● Imprim el valor de la clave peso usando el método get
'''
Persona = {"edad":20, "peso":75, "nombres":"Pedro", "apellidos":"Pérez Pérez"}
print("Claves del diccionario:\n")
print ("----------------------------------------")
for key in Persona.keys():
	print ("Llave",key)
print ("----------------------------------------\n")
for value in Persona.values():
    print("Valor: ", value)
Persona["peso"]=77
Persona["edad"]=21
Persona.pop("apellidos")
print("llave peso: ", Persona.get("peso"))