# Cifrado César.
text = input("Ingresa tu mensaje: ")
num = int(input("Ingresa el número de desplazamiento: "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + num

    if code > ord('Z') and char.isupper():
        lo_que_le_falta = code - ord('Z')
        code = ord('A') + lo_que_le_falta - 1
    elif code > ord('z') and char.islower():
        lo_que_le_falta = code - ord('z')
        code = ord('a') + lo_que_le_falta - 1
    cipher += chr(code)

print(cipher)
   