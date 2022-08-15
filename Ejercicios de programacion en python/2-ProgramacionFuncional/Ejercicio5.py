# Escribir una función que reciba una frase y devuelva
# un diccionario con las palabras que contiene y su longitud.


def longitud(frase):
    diccionario = {}
    f = frase.split()
    for palabra in f:
        diccionario[palabra] = len(palabra)
    return diccionario


print(longitud('Hola mundo mi nombre es angel'))
