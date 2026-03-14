#La sentencia continue – el Feo Devorador de Vocales

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingrese una palabrsa: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue 
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else : print(letter)

    # Completa el cuerpo del bucle for.

#La sentencia continue – el Lindo Devorador de Vocales

word_without_vowels = ""
user_word = input("Ingrese una palabrsa: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue 
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else: word_without_vowels += letter

print(word_without_vowels)