def mysplit(strng):
    cadena = []
    word = ""
    j = 0
    for i in range(len(strng)):
        word = word + strng[i]
        if i+1 < len(strng) and strng[i+1] == " " :
            word = word.strip()
            cadena.append(word)
            j += 1
            word = ""
    for i in range(len(cadena)-1, -1, -1):
        if cadena[i] == "":
            del cadena[i]
    return cadena



print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))