word = input("Dame la palabra que quieres buscar: ").upper()
strn = input("Dame la cadena en donde la quieres buscar: ").upper()

found = False
start = 0
for i in strn:
    if word[start] == i:
        start += 1
        if start == len(word):
            found = True
            break
if found:
    print("Si")
else:
    print("No")