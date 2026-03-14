def is_anagrama(cadena1, cadena2):
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()

    return sorted(cadena1) == sorted(cadena2)
cadena1 = input("Dace una cadena: ")
cadena2 = input("Dace otra cadena: ")
if is_anagrama(cadena1, cadena2):
    print("Son anagramas")
else:
    print("No son anagramas")