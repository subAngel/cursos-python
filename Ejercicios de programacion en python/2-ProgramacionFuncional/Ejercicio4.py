# Escribir una función que reciba otra función booleana y una lista, y
# devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.

def only_true(fun, lista):
    l = []
    for i in lista:
        if fun(i):
            l.append(i)
    return l


def impar(n):
    return n % 2 == 1


print(only_true(impar, [1, 2, 3, 4, 5, 6, 7, 8]))
