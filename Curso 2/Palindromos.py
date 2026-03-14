def es_palindromo(cadena):
    cadena =cadena.upper()
    cadena = cadena.replace(" ", "")
    #print(cadena) checando que hace el codigo
    for i in range(len(cadena) // 2):
        if cadena[i] == cadena[-i-1]:
            continue
        else:
            return False
    return True
cadena = input("Inserte una cadena para ver si es un palíndromo: ")
if es_palindromo(cadena):
    print("Es un palíndromo")
else:
    print("Lo siento viejo no es palindromo")