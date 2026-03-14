income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.
else :
	exedente = income - 85528
	tax = 14839.02 + exedente *0.32
tax = round(tax, 0)
if tax>0:print("El impuesto es:", tax, "pesos")
else:print("El impuesto es: 0.0 pesos")