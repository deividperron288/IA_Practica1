x = int(input("Ingresa un numero para la hipotesis:"))
pasos = 0
while True:

    if x % 2 == 0:
        x //= 2
        print(x)
    elif x!=1 :
        x = x * 3 + 1
        print(x)
    if x == 1:
        pasos+=1
        break
    pasos +=1

print("pasos: ", pasos)
