'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
'''


def frecuencia(cadena):
    dict = {}
    cadena= cadena.split()
    for x in cadena:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    return dict


def mas_repetida(dict):
    palabra = ''
    frecuencia = 0
    for word, frec in dict.items():
        if frec > frecuencia:
            palabra = word
            frecuencia = frec
    return palabra, frecuencia


texto = "Una multitud extranada de inmortales hambrientos con sed de sangre de con de de de multitud"
print(frecuencia(texto))
print(mas_repetida(frecuencia(texto)))
