# !/usr/bin/python
# -*-coding: utf-8-*-

#Alejandro López	
#isx43567395	
#11/10/2018	
#Versión final

#Que hace el script --> Programa que reciba una entrada con segundos en formato entero y convertirlo en formato H:M:S 
#Especificaciones de Entrada.
#Horas y minutos valor asignado a 0 y pedimos segundos con valor entero.

#Pedir al usuario los segundos.
segundos=int(input('Introduce segundos: '))

#Calcular los segundos que pasan de 60, restar el sobrante a los segundos totales y sumar el sobrante a los minutos.
segundos_aumentados = (segundos // 60)

segundos_totales = segundos - segundos_aumentados*60
 
#Calcular los minutos que pasan de 60, restar el sobrante a los minutos totales y sumar el sobrante a las horas.

minutos = segundos_aumentados

minutos_aumentados = (minutos // 60)

minutos_totales = minutos - minutos_aumentados*60

#Sumar los minutos sobrantes a las horas.

horas_totales = minutos_aumentados

#Mostramos horas, minutos y segundos en el formato correcto.

print ("Tiempo en formato correcto:",horas_totales, "horas,", minutos_totales, "minutos, ", segundos_totales, "segundos")

