# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#07/10/2018	
#Version final

#Que hace el script --> Programa que lee el nombre del trabajador,las horas trabajadas, el precio que cobra por hora, salario bruto y salario neto.
#Especificaciones de Entrada.
#Nombre del trabajador,horas trabajadas, dinero que cobra por hora.

#Nombre, horas trabajadas y precio por hora.
nombredeltrabajador= 'Alfredo'

horastrabajadas = 160

precioporhora= 10

#Operaciones, sueldo bruto, descuento en concepto de renta y sueldo neto
sueldobruto= horastrabajadas * precioporhora


descuentoderenta= sueldobruto*10/100

sueldoneto= sueldobruto-descuentoderenta


#Para mostrar por pantalla nombre, sueldo bruto y descuento de renta y sueldo a pagar.
print ('Nombre del trabajador ', nombredeltrabajador )
print ('Sueldo bruto ', sueldobruto, '€')
print ('Descuento de renta ', descuentoderenta, '€')

print ('Sueldo a pagar', sueldoneto, '€' )

