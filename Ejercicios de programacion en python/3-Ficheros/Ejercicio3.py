# Escribir una función que pida dos números n y m entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
# y muestre por pantalla la línea m del fichero.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


def mostrar_linea(n, linea):
    filename = 'tabla-{}.txt'.format(n)
    try:
        with open('tabla-{}.txt'.format(n), 'r') as archivo:
            lineas = archivo.readlines()
        print(lineas[linea-1])
    except FileNotFoundError:
        print('No existe el archivo de la tabla')


entrada = int(input('Ingrese un numero para imprimir la tabla: '))
linea = int(input('Ingrese la linea que quiera ver: '))
mostrar_linea(entrada, linea)