

descuento = 0
total_pagar = 0
IVA = 0.19
consumo = int(input("Consumo en el restaurante: "))

if consumo < 100:
    descuento = 0.10
elif 100 <= consumo < 200:
    descuento = 0.20
elif consumo >= 200:
    descuento = 0.30

total_descuento = consumo - consumo*descuento
total_final = total_descuento + total_descuento*IVA

print('----------------------------')
print('----------FACTURA-----------')
print('----------------------------')
print('Consumo:             {}'.format(consumo))
print('Descuento:           {}'.format(descuento))
print('Monto con descuento: {}'.format(total_descuento))
print('Monto Final:         {}'.format(total_final))
print('----------------------------')

