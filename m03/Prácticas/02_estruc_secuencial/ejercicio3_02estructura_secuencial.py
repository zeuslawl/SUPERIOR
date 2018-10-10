# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#07/10/2018	
#Versión final

#Que hace el script --> Programa que pida precio de articulo y calcule su valor aplicando el 13% de iva.
#Especificaciones de Entrada.
#Precio en número entero.

#Precio que pone el usuario.
precio=float(input('Precio del producto: '))


#Operaciones 
iva= precio*13/100

preciofinal= iva+precio 

#Muestra precio sin iva, iva y su valor final.
print ('Precio sin iva ', precio,'€' )

print ('Iva ', iva,'€' )

print ('Precio final con iva incluido ', preciofinal,'€' )
