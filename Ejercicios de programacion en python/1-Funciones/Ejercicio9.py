'''
Escribir una función que calcule el máximo común divisor
de dos números y otra que calcule el mínimo común múltiplo.
'''


def MCD(n1, n2):  # Maximo Comun Divisor
    while n2 > 0:
        rest = n2
        n2 = n1 % n2
        n1 = rest
    return rest


def MCM(n1, n2):
    return (n1 * n2) // MCD(n1, n2)


n1 = int(input("Ingrese el primer numero: "))

n2 = int(input("ingrese el segundo numero: "))

print("MCD es {}".format(MCD(n1,n2)))
print("MCM es {}".format(MCM(n1,n2)))