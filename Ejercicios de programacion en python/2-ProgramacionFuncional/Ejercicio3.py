
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
# resultado de aplicar la función dada a cada uno de los elementos de la lista.


def aplicar_fun(funcion, lista):
    '''funcion que aplica una funcion a toods los elementos de una lista.

    Paramettros:
        funcion> es una funcion
        lista> devuelve una lista con valores que se pasan como argumentos a la funcion.
    '''
    list = []
    for i in lista:
        list.append(funcion(i))
    return list


def mitad(n):
    return n/2


print(aplicar_fun(mitad, [1,2,3,4,5,6,7]))