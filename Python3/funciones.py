# variable = 1 # variable global
#
#
# def fun1(a, b): # a y b son variables locales
#     variable = 2
#     return a+b
#
# print(variable)
#
# archivo = open('archivo_prueba.txt')
#
# lineas = archivo.readlines()
#
# for linea in lineas:
#     print(linea)
#
# archivo.close()
#
#
# with open('archivo_prueba.txt') as archivo:
#     lineas = archivo.readlines()
#     for linea in lineas:
#         print(linea)


with open('file.txt', 'w+') as archivo:
    texto = 'hola mundo'
    archivo.write(texto)
