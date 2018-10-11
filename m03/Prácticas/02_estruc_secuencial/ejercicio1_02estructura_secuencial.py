# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#07/10/2018	
#Versión final

#Que hace el script --> Asignar 3 sueldos de 3 empleados y aplicarles un aumento del 10,12 y 15% respectivamente.
#Especificaciones de Entrada
# Números enteros.

#Asignación de sueldo en variables
sueldo1=float(input('Introduce el primer sueldo : '))
sueldo2=float(input('Introduce el segundo sueldo: '))
sueldo3=float(input('Introduce el tercer sueldo: '))


#Operaciones de aumentos de sueldo 10%,12% y 15% respectivamente.
aumento10= (sueldo1*10/100) + sueldo1

aumento12=(sueldo2*12/100) + sueldo2

aumento15= (sueldo3*15/100) + sueldo3
 



print ('Sueldos iniciales ', sueldo1,sueldo2,sueldo3 )
print ('El resultado despues de aplicar el aumento del 10% es ', aumento10)
print ('El resultado despues de aplicar el aumento del 12% es ', aumento12)

print ('El resultado despues de aplicar el aumento del 15% es ', aumento15 )

