fila =[]
for i in range(9):
    fila.append("")
    fila [i]= input(f"Dame la fila con 9 digitos numero {i+1} pal Sudoku: ")
    fila[i] = str(fila[i])
    while len(fila[i]) != 9:
        fila [i]= input("La fila debe contener exactamente 9 dígitos.\n" \
                    f"Dame la fila con 9 digitos numero {i+1} pal Sudoku: ")

for i in range(9):
    for j in range(9):
        sabe = ord("0") + j +1
        check = 1 == fila[i].count(chr(sabe))
        #print(check,f"fila {i}: existen {fila[i].count(chr(sabe))} : {j+1}")
        if check == False:
            print("No es un Sudoku")
            exit()   
for j in range(9):
    for i in range(9):   
        for k in range(9): 
            if i != k and fila[i][j] == fila[k][j]:
                print("NNo es un Sudoku")
                exit()
print("Es un Sudoku")