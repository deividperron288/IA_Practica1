my_list = [2,2,2,2,2,4,1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 10,2,8,7,10,4]
#
# Escribe tu código aquí.
i = 0
j = 0
while j < len(my_list):
    #print(j,i)
    if my_list[i] == my_list[j] and i != j:
        del my_list[j]
        #print(f" n = {j} m = {i}") #probando en que posiciones se elimino
    i +=1
    if i > (len(my_list) - 1):
        i = 0
        j +=1

print("La lista con elementos únicos:")
print(my_list)