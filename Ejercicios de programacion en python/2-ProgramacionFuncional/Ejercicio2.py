
'''
Escribir una función que simule una calculadora científica que permita calcular
el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará
al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los
enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
'''

from math import sin, cos, tan, exp, log

def apply_fun(fun, x):
    functions = {'sin':sin, 'cos':cos, 'tan':tan,'exp':exp,'log':log}
    result = {}
    for i in range(1, x+1):
        result[i] = functions[fun](i)
    return result


def calculadora():
    f = input('Intruduce la funcion a aplicar (sin,cos,tan,exp,log): ')
    n = int(input('Ingresa un numero entero positivo: '))
    for i, j in apply_fun(f, n).items():
        print(i,'\t',j)
    return

calculadora()