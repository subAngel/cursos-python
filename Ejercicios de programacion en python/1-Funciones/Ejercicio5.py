'''
Escribir una función que calcule el área de un círculo y otra que calcule
el volumen de un cilindro usando la primera función.
'''


def AreaC(radio):  # pi * r^2
    area = 3.1415 * radio ** 2
    return area


def VolumenCil(radio, altura):
    volumen = AreaC(radio) * altura
    return volumen


print("Area del circulo: {}".format(AreaC(3)))
print("Volumen del cilindro: {}".format(VolumenCil(3, 5)))
