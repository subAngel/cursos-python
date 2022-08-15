'''
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
'''


def cuadrados(lista):
    cuad = []
    for x in lista:
        cuad.append(x ** 2)
    return cuad


print(cuadrados([1, 2, 3, 4, 5]))
