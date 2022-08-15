# Uso de while en python

# Repeticion de numeros
numero = 1
'''
while numero <= 10:
    print(numero)
    numero += 1
'''

# Repeticion de numero con break
'''
while numero <= 10:
    print(numero)
    if numero == 6:
        break
    numero += 1
'''

numero = 0
# Repeticion While de numero con CONTINUE
'''
while numero <= 10:
    numero += 1
    if numero == 5:
        continue
    print(numero)
'''

# SUma de numeros naturales
numeros = int(input("Ingrese un numero: "))
resultado, control = 0, 1
while control <= numeros:
    resultado += control
    control += 1
print(resultado)
