# Ejercicio 1: Definir una función max() que tome como argumento dos números
# y devuelva el mayor de ellos. (Es cierto que python tiene una función max()
# incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(num1, num2):
    if num1 > num2:
        return print("{} es mayor".format(num1))
    elif num1 < num2:
        return print("{} es mayor".format(num2))
    else:
        return print("{} y {} son iguales".format(num1, num2))


''' Ejercicio 2:
    Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
'''


def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    elif n1 == n2 and n2 > n3:
        return n1
    elif n2 == n3 and n2 > n1:
        return n2
    else:
        return n1


''' Ejercicio 3:
    Definir una función que calcule la longitud de una lista o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, pero escribirla por 
    nosotros mismos resulta un muy buen ejercicio.'''


def longitud(cadena):
    cont = 0
    for x in cadena:
        cont += 1
    return cont


''' Ejercicio 4:
    Escribir una función que tome un carácter y devuelva 
    True si es una vocal, de lo contrario devuelve False'''


def isVocal(char):
    if char in 'aeiou' or char in 'AEIOU':
        return True
    else:
        return False


''' Ejercicio 5:
    Escribir una función sum() y una función multip() que sumen y multipliquen 
    respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) 
    debería devolver 10 y multip([1,2,3,4]) debería devolver 24.'''


def sum(lista):
    resul = 0
    for x in lista:
        resul += x
    return resul


def multip(lista):
    aux = lista[0]
    for x in lista:
        aux *= x
    return aux


''' Ejercicio 6
    Definir una función inversa() que calcule la inversión de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''


def inversa(cadena):
    nueva = ''
    for x in cadena[::-1]:
        nueva += x
    return nueva


''' Ejercicio 7
    Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el 
    mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''


def es_palindromo(cadena):
    cadena = cadena.lower()
    if cadena == cadena[::-1]:
        return True
    else:
        return False


''' Ejercicio 8
    Definir una función superposicion() que tome dos listas y devuelva True si 
    tienen al menos 1 miembro en común o devuelva False de lo contrario. 
    Escribir la función usando el bucle for anidado.'''


def superposicion(l1, l2):
    lista1 = set(l1.lower().split())
    lista2 = set(l2.lower().split())
    if lista1 & lista2:
        return True
    else:
        return False


''' Ejercicio 9
     Definir una función generar_n_caracteres() que tome un entero n y 
     devuelva el caracter multiplicado por n. 
     Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''


def generar_n_caracteres(i, char):
    return char*i


''' Ejercicio 10
    Definir un histograma procedimiento() que tome una lista de números enteros e 
    imprima un histograma en la pantalla. 
    Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
    ****
    *********
    *******                             '''


def procedimiento(lista):
    for x in lista:
        print(x*'*', end='\n')

# ------------------------------------- PRUEBAS ------------------------------------------
max(5, 5)  # Ejercicio 1

print(max_de_tres(5, 5, 5))  # Ejercicio 2

print(longitud("hola mi nombre es angel")) # Ejercicio 3

print(isVocal('A'))     # Ejercicio 4

print(sum([1,2,3,4,5]), end = ' ')  # Ejercicio 5
print(multip([1,2,3,4]))

print(inversa("Hola mundo")) # Ejercicio 6

print(es_palindromo("Radar")) # Ejercicio 7

print(superposicion("Hola soy angel", "jesus es mi nombre")) # ejercicio 8

print(generar_n_caracteres(5, 't'))     # ejercicio 9

procedimiento([5,2,8,5,9])
