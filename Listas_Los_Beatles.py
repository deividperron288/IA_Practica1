# paso 1
beatles = []
print("Paso 1:", beatles)
# paso 2
beatles.append("John Lennon")
beatles.append("Paul Mcarney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

# paso 3
for i in range(2):
    beatles.append(input("Agrege a Stu Sutcliffe y a Pete Best de a uno por solicitud:\n"))
print("Paso 3:", beatles)
# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(4,"Ringo Star")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
