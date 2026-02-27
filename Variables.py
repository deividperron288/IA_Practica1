
'''Escenario
A continuación una historia:

Érase una vez en la Tierra de las Manzanas, 
Juan tenía tres manzanas, 
María tenía cinco manzanas, y 
Adán tenía seis manzanas. 
Todos eran muy felices y vivieron por muchísimo tiempo. 
Fin de la Historia.

Tu tarea es:

Crear las variables: john, mary, y adam;
Asignar valores a las variables. 
El valor debe de ser igual al número de manzanas que cada quien tenía;
Una vez almacenados los números en las variables, 
imprimir las variables en una línea, y separar cada una de ellas 
con una coma;
Después se debe crear una nueva variable llamada total_apples 
y se debe igualar a la suma de las tres variables anteriores;
"Número total de manzanas:" y total_apples.'''
john = 3
mary = 5
adam = 6
print(f"{john}, {mary}, {adam}")
total_apples = john + mary + adam
print(f"Manzanas totales = {total_apples}")

'''Escenario
Millas y kilómetros son unidades de longitud o distancia.

Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, 
complementa el programa en el editor para que convierta de:

Millas a kilómetros;
Kilómetros a millas.
No se debe cambiar el código existente.
Escribe tu código en los lugares indicados con ###.
Prueba tu programa con los datos que han sido provistos en el código fuente
Pon mucha atención a lo que esta ocurriendo dentro de la función print().
Analiza como es que se proveen múltiples argumentos para la función,
y como es que se muestra el resultado.
'''
kilometers = 12.25
miles = 7.38

miles_to_kilometers =  miles_to_kilometers = miles * 1.61 
kilometers_to_miles =  kilometers_to_miles = kilometers / 1.61 

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")