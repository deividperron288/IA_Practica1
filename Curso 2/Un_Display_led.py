'''Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
Nota: el número 8 muestra todas las luces LED encendidas.

Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.

Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.'''
def separar_digitos(num):
    digitos = []
    
    for d in str(num):
        digitos.append(int(d))
        
    return digitos
def display_led(num):
   # ["###","#  ","  #","# #"]
    digits = [
        [0,1,2,3,4,5,6,7,8,9],
        ["###","  #","###","###","# #","###","###","###","###","###"],
        ["# #","  #","  #","  #","# #","#  ","#  ","  #","# #","# #"],
        ["# #","  #","###","###","###","###","###","  #","###","###"],
        ["# #","  #","#  ","  #","  #","  #","# #","  #","# #","  #"],
        ["###","  #","###","###","  #","###","###","  #","###","  #"],
    ]
    digitos_separados = separar_digitos(num)
    for fila in range(6):
        for digitos in digitos_separados:
            print(digits[fila][digitos],end=" ")
        print()

num = int(input("Ingrese un número entero no negativo: "))

display_led(num)