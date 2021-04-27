''' 
programa que pida al usuario el nombre de un producto existente en una tienda, luego, que le muestre
el precio del producto. El usuario debe poder elegir de entre por lo menos cinco productos. Use diccionarios.
'''
Productos = {'Detergente':2500,'Golocinas':800,'Aceite':3800,'Pilas':2750,'Condones':500,}
print("Productos en la tienda son:\n")
print ("----------------------------------------")
for i in Productos:
	print (i)
print ("----------------------------------------\n")	
dato = str(input("Ingrese el producto como aparece en el listado: \n"))
print ("el valor de",dato,"es de:",Productos[dato])