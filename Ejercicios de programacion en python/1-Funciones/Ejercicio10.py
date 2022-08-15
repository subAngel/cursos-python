'''
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
'''


def dec_to_bin(numero):
    binario = []
    while numero > 0:
        binario.append(str(numero%2))
        numero //= 2
    binario.reverse()
    return "".join(binario)


def bin_to_dec(numero):
    num = list(numero)
    num.reverse()
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i])* 2 ** i
    return decimal


print(dec_to_bin(10))
print(bin_to_dec("10101"))