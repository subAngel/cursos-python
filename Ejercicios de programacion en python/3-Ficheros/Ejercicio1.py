# Escribir una función que pida un número entero entre 1 y 10
# y guarde en un fichero con el nombre tabla-n.txt la tabla de
# multiplicar de ese número, done n es el número introducido.


def tabla(n):
    with open('tabla-{}.txt'.format(n), 'w+') as archivo:
        for x in range(10):
            linea = '{} x {} = {}\n'.format(n, x + 1, (x + 1) * n)
            archivo.write(linea)


numero = int(input("Ingrese un numero para la tabla: "))
tabla(numero)
