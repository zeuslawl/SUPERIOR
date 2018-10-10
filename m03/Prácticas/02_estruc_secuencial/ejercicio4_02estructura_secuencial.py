# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#07/10/2018	
#Versión final

#Que hace el script --> Programa que pida horas, minutos y segundos con valor entero y pasarlos al formato correcto.
#Especificaciones de Entrada.
#Horas, minutos y segundos con valor entero

#Pedir al usuario horas, minutos y segundos
horas=int(input('Introduce horas: '))
minutos=int(input('Introduce minutos: '))
segundos=int(input('Introduce segundos: '))


#Calcular los segundos que pasen de 60 y pasarlos a los minutos.
segundos_aumentados = (segundos // 60)

segundos_totales = segundos - segundos_aumentados*60
 
#Calcular los minutos que pasen de 60 y pasarlos a las horas.
minutos = minutos + segundos_aumentados

minutos_aumentados = (minutos // 60)

minutos_totales = minutos - minutos_aumentados*60


#Sumar los minutos restantes a las horas.

horas_totales = horas + minutos_aumentados

#Mostramos horas, minutos y segundos en el formato correcto.

print ("")
print ("Tiempo en formato correcto:",horas_totales, "horas,", minutos_totales, "minutos, ", segundos_totales, "segundos")
print ("")
