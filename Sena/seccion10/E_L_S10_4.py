''' 
programa que cumpla con los siguientes requerimientos: En una clínica, se requiere un programa
donde el usuario pueda consultar el día de su cita mediante su documento.
La cita debe tener día y fecha. Si el usuario consulta, el programa debe mostrarle
sus nombres, seguidos del día y hora de su cita.
Una vez hecha laconsulta, el programa le debe mostrar al usuario un mensaje preguntándole
si desea cambiar el día ó fecha de su cita, de ser así el programa debe realizar tal cambio
y mostrarle al usuario que el cambio solicitado ha sido exitoso. Use diccionarios.
'''
import sys
Pacientes = {1:['lola','01/30/2021','10:35'],
			 2:['lole','02/24/2021','10:55'],
			 3:['loli','03/24/2021','11:15'],
			 4:['lolo','04/25/2021','11:35'],
			 5:['lolu','05/26/2021','11:55'],
			 }
Docu = int(input("Ingrese el Documento:"))
print ("----------------------------------------")
print ("Nombre del Paciente:",Pacientes[Docu][0])
print ("Fecha de la cita:",Pacientes[Docu][1])
print ("Hora:",Pacientes[Docu][2])
print ("----------------------------------------")
pre=str(input("¿Decea cambiar la fecha y hora de la cita S/N?: "))
if ((pre=='S') or (pre=='s')):
	Pacientes[Docu][1]=str(input("¿ingrese la nueva fecha dd/mm/aaaa: "))
	Pacientes[Docu][2]=str(input("¿ingrese la nueva Hora de cita hh:mm: "))
	print ("----------------------------------------")
	print ("Nombre del Paciente:",Pacientes[Docu][0])
	print ("Fecha de la cita:",Pacientes[Docu][1])
	print ("Hora:",Pacientes[Docu][2])
	print ("----------------------------------------")
	sys.exit()
else:
	sys.exit()