'''Escenario
Tu tarea es completar el código para evaluar los
 resultados de cuatro operaciones aritméticas básicas.
Los resultados deben imprimirse en la consola.
Es posible que no puedas proteger el código de un usuario
 que quiera dividir entre cero. 
 Está bien, no te preocupes por eso por ahora.'''

# ingresa un valor flotante para la variable a aquí
a = float(input("A: "))
# ingresa un valor flotante para la variable b aquí
b = float(input("B: "))
# mostrar el resultado de la suma aquí
print("\nSuma =", a + b)
# mostrar el resultado de la resta aquí
print("Resta =", a - b)  
# mostrar el resultado de la multiplicación aquí
print("Multiplicación =", a * b)
# mostrar el resultado de la división aquí
print("División =",round (a/b,3) )
print("\n¡Eso es todo, amigos!")