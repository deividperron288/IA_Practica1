hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
Total_mins = mins + dura
min_finales = Total_mins % 60
horas_agregadas = (Total_mins)//60
#print(horas_agregadas)
horas_finales = hour + horas_agregadas
print (horas_finales ,":",min_finales)
