# Escribir una función que pida un número entero entre 1 y 10,
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese
# número, done n es el número introducido, y la muestre por
# pantalla. Si el fichero no existe debe mostrar un mensaje
# por pantalla informando de ello.


def mostrar_tabla(n):
    filename = 'tabla-{}.txt'.format(n)
    try:
        with open('tabla-{}.txt'.format(n), 'r') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print('No existe el archivo de la tabla')


entrada = int(input('Ingrese un numero para imprimir la tabla: '))
mostrar_tabla(entrada)

