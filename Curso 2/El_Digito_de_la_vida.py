'''Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

1 Enero 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 es el dígito que buscamos y encontramos.'''
#funcion ya usada en el display led
def separar_digitos(num):
    digitos = []
    
    for d in str(num):
        digitos.append(int(d))
        
    return digitos
def digito_de_la_vida(fecha):
    digitos_separados = separar_digitos(fecha)
    suma = sum(digitos_separados)
    
    while suma >= 10:
        digitos_suma = separar_digitos(suma)
        suma = sum(digitos_suma)
        
    return suma
fecha = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
fecha_pegada = fecha.replace("/","")
print("El dígito de la vida es:", digito_de_la_vida(fecha_pegada))