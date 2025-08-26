from datetime import datetime

#Sacamos la fecha actual
fecha_actual = datetime.now()
#Obtener el día de la semana y  el número de día
dia_semana = fecha_actual.strftime("%A") #Nombre del día
numero_dia = fecha_actual.day #Número del dia

print("Hoy es", dia_semana, "y el dia es", numero_dia)
print("Saúl \"canelo\" Álvarez")

