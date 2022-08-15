def descuento(precio, descuento):
    return precio - precio*(descuento)/100


def iva(precio, porcentaje):
    return precio + precio*(porcentaje)/100


def calcular_total(dict, funcion):
    total = 0
    for precio, descuento in dict.items():
        total += funcion(precio, descuento)
    return total


precios = {1000:20, 2314:12,4144:21}
print(calcular_total(precios, descuento))
print(calcular_total(precios, iva))