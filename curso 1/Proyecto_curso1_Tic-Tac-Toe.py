import random
def imp_cuadricula(valor):
        print( " ---+---+----+ ")
        print(f" | {valor[0]} | {valor[1]} | {valor[2]} | ")
        print( " ---+---+----+ ")
        print(f" | {valor[3]} | {valor[4]} | {valor[5]} | ")
        print( " ---+---+----+ ")
        print(f" | {valor[6]} | {valor[7]} | {valor[8]} | ")
        print( " ---+---+----+ \nSiguiente Turno...")

def insert_jugador(valor):
    while True:
        posicion = int(input("Juega en una posicion(1 al 9): "))
        if valor[posicion-1] == "X" or valor[posicion-1] == "O":
            print("Posición ocupada, elige otra posición")
            continue
        else:
            valor[posicion-1] = "X"
            break
    imp_cuadricula(valor)

def insert_computadora(valor):
    while True:
         
        n = random.randint(0, 8)
        if valor[n] != "X" and valor[n] != "O":
            valor[n] = "O"
            print("Se coloco en la posicion ", n +1)
            break
    imp_cuadricula(valor)

def comprobar_victoria(valor):
    for i in range(0, 9, 3):
        if valor[i] == valor[i+1] == valor[i+2] =="X":
            print("¡Has ganado!\n"*3)
            return True

    for i in range(3):
        if valor[i] == valor[i+3] == valor[i+6] == "X":
            print("¡Has ganado!\n"*3)
            return True

    if valor[0] == valor[4] == valor[8] == "X":
        print("¡Has ganado!\n"*3)
        return True

    if valor[2] == valor[4] == valor[6] == "X"  :
        print("¡Has ganado!\n"*3)
        return True
    for i in range(0, 9, 3):
        if valor[i] == valor[i+1] == valor[i+2] =="X":
            print("¡Has ganado!\n"*3)
            return True
#Comprueba derrota 
    for i in range(3):
        if valor[i] == valor[i+3] == valor[i+6] == "O":
            print("Perdiste*\n"*3)
            return True
    for i in range(0, 9, 3):
        if valor[i] == valor[i+1] == valor[i+2] =="O":
            print("Perdiste\n"*3)
            return True

    if valor[0] == valor[4] == valor[8] == "O":
        print("Perdiste*\n"*3)
        return True

    if valor[2] == valor[4] == valor[6] == "O":
        print("Perdiste*\n"*3)
        return True

    return False
         
        


valor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
imp_cuadricula(valor)
valor[4] = "O"
imp_cuadricula(valor)
count = 1
ganar = False
while ganar == False:
    count +=1
    insert_jugador(valor)
    ganar = comprobar_victoria(valor)
    if ganar == True: break
    insert_computadora(valor)
    ganar = comprobar_victoria(valor)
    if ganar == True: break
    if count == 9: break
print("Se acabo el juego")
