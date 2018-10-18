# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#17/10/2018	
#Versión final

#Que hace el script --> Programa generico para conversiones.
#Especificaciones de Entrada
# Variables en float.

#Asignación de cm

factor_conversion= 0.39737 #De cm a pulgadas

#Leer cantidad

c_inicial=float(input())

#Operación de la conversión de cm a pulgadas

c_final= c_inicial*factor_conversion

#Mostramos resultado por pantalla
print (c_final)
