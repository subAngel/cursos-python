# Escribir un proigrama que acceda a un fichero de internet medinte su url
# y muestre por pantalla el numero de palabras que contiene


def contar_palabras(url):
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as fichero:
            contenido = fichero.read()
    except URLError:
        print('La URL no existe')
    else:
        return len(contenido.split())


url = 'https://www.gutenberg.org/files/2000/2000-0.txt'

print(contar_palabras('https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html'))
