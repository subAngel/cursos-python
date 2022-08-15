# Descuentos de un restaurante

def monto(cantidad):
    monto_final = 0
    if cantidad <= 1000:
        monto_final = cantidad - cantidad*0.10    # 10% de descuento
    elif cantidad > 1000:
        monto_final = cantidad - cantidad*0.20    # 20% de descuento
    return monto_final + monto_final*0.19

cuenta = int(input("Cuanto gastó en nuestro restaurante? "))
print("Cuenta Final: {:3}".format(monto(cuenta)))