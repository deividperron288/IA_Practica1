blocks = int(input("Ingresa el número de bloques: "))
#
# Escribe tu código aquí.
#	
altura = 0
i = 0
bloks_usados = 0
while bloks_usados< blocks:
   bloks_usados = bloks_usados + i
   if bloks_usados> blocks : break
   i += 1 
if i != 0 :altura = i-1

print("La altura de la pirámide:", altura)