# funcion que calcule los modulos de una funcion.


def sum_square(x, y):
    # Recibe dos parametros, y calcula la suma del primero mas el cuadrado de la segunda
    return x+y**2


def modulo(v):
    # Funcion que calcula el modulo de un vector
    from functools import reduce
    return reduce(sum_square,v, 0)**0.5


print(modulo((3, 4)))
print(modulo((1,2,3)))