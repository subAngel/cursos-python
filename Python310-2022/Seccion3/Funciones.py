# Funciones en python
def funcion():
    print("Funcion")


def suma(num1, num2):
    print(num1 + num2)


def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


# entrada = int(input("Ingrese un numero para el factorial: "))
# print("El factorial de", entrada, "es", factorial(entrada))

def numero_positivo(num):
    if num > 0:
        print(num, "es positivo")
    elif num < 0:
        print(num, "es negativo")
    elif num == 0:
        print("Es cero")


def ciclo(n):
    while n <= 10:
        print(n)
        n += 1


