# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#18/10/2018	
#Versión final

#----------------------------------------------------------------------------------------------------------------
#Que hace el script 
#Fes un programa que faci conversions de base b a base 10.
#Ha de llegir un nombre que serà la base i 3 dígits (per exemple) un a un. Ha de retornar el nombre en base 10.
#Exemple: base = 3  dígits = 0, 1, 2  (012) 			sortida:5
#---------------------------------------------------------------------------------------------------------------

#----------------------------
#Especificaciones de Entrada
#Entrar número entero del 2 al 10 como base.
#Entrar 3 números enteros >=0 y menores a la base.
#base > numero1 and base > numero2 and base > numero3 and numero1 >= 0 and numero2 >= 0 and numero3 >= 0
#----------------------------

base= int(input('¿Con que base quieres calcular? '))

primer_numero = int(input("Primer número? "))
segundo_numero = int(input("Segundo número? "))
tercer_numero = int(input("Tercer número? "))

pos2 = primer_numero*base**2
pos1 = segundo_numero*base**1
pos0 = tercer_numero*base**0

resultado = pos0 + pos1 + pos2

#Mostramos el resultado
print(resultado)
