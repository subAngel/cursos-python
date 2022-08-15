'''
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
'''


def media(lista):
    total = 0
    for x in lista:
        total += x
    return total/len(lista)


listita = [6, 7]
numeros = input("Ingrese una lista de numeros [1,2,3,4]: ")
numeros = list(numeros.split(","))
numeros = list(map(int,numeros))
print(media(numeros))
print(media(listita))