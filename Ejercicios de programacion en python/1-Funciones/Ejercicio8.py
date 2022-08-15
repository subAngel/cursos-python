'''
Escribir una función que reciba una muestra de números en una lista y
devuelva un diccionario con su media, varianza y desviación típica.
'''
import math


def diccionario(*lista):
    dict = {"Media": None, "Varianza": None, "Desviacion": None}
    media, var, desv = 0, 0, 0
    for x in lista:
        media += x
    media = media / len(lista)
    for i in lista:
        var = + (i - media)
    var = var/len(lista)
    desv = math.sqrt(var)
    dict.update({"Media": media})
    dict.update({"Varianza": var})
    dict.update({"Desviacion": desv})
    return dict


print(diccionario(1, 2, 3, 4, 5))
