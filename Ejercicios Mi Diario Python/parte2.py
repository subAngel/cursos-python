""" Ejercicio 1
    La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del
    ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos
    que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función
    max_in_list() que tome una lista de números y devuelva el mas grande.
"""


def max_in_list(lista):
    mayor = 0
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor


''' Ejercicio 2
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.'''


def mas_larga(cadena):
    lista = cadena.split()
    word = ''
    for palabra in lista:
        if len(palabra) > len(word):
            word = palabra
    return word


''' Ejercicio 3
    Escribir una función filtrar_palabras() que tome una lista de palabras y 
    un entero n, y devuelva las palabras que tengan mas de n caracteres.'''


def filtrar_palabras(cadena, n):
    lista = cadena.split()
    salida = []
    for palabra in lista:
        if len(palabra) >= n:
            salida.append(palabra)
    return salida


''' Ejercicio 4
    Escribir un programa que le diga al usuario que ingrese una cadena. 
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.'''


def contarMayus():
    import string
    cadena = input("Ingrese una cadena de texto: ")
    mayusculas = string.ascii_uppercase
    contador = 0
    for letra in cadena:
        if letra in mayusculas:
            contador += 1
    print("La cadena tiene {} mayusculas.".format(contador))


''' Ejercicio 5
    Construir un pequeño programa que convierta números binarios en enteros.'''


def bin_to_int(binario):
    lista = list(binario)
    numero = 0
    lista.reverse()
    for x in range(len(lista)):
        numero += int(lista[x]) * 2 ** x
    return "{}b es equivalente a {}d".format(binario, numero)


''' Ejercicio 6
    Escribir un pequeño programa donde:
        - Se ingresa el año en curso.
        - Se ingresa el nombre y el año de nacimiento de tres personas.
        - Se calcula cuántos años cumplirán durante el año en curso.
        - Se imprime en pantalla.'''


def cumple():
    current_year = int(input("ingresa el año actual: "))
    for i in range(3):
        nombre = input("Nombre: ")
        nacimiento = int(input("Año de nacimiento: "))
        print("{} cumplira {} en {}".format(nombre, current_year - nacimiento, current_year))


''' Ejercicio 7
    Definir una tupla con 10 edades de personas.
    Imprimir la cantidad de personas con edades superiores a 20.
    Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.'''


def edad_superior(edades, edad):
    contador = 0
    for x in edades:
        if x >= edad:
            contador += 1
    return print(contador, "personas arriba de ", edad)


''' Ejercicio 8 
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar. '''


def contar_nombres(conjunto):
    letra = input("ingresa una letra para buscar nombres: ")
    cant = 0
    for nombre in conjunto:
        if nombre[0] == letra.upper():
            cant += 1
    return cant


''' Ejercicio 9
    Crear una función contar_vocales(), que reciba una palabra y cuente 
    cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.'''


def contar_vocales():
    palabra = input("Ingrese una palabra: ")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return print("hay {} vocales en {}".format(contador, palabra))


''' Ejercicio 10
    Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
    Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400'''


def is_bisiesto(year):
    if year%4 == 0 and (not(year%100 == 0)):
        return True
    else:
        return False

# ------------------------------ PRUEBAS ----------------------------------------

print(max_in_list([1, 4, 5, 2, 9, 10, 3]))  # Ejercicio 1

print(mas_larga("Hola soy unapalabralarga"))  # Ejercicio 2

print(filtrar_palabras("hola mi nombre es angel y esto es un ejemplo de frase", 5))  # Ejercicio 3

# contarMayus()   # Ejercicio 4

print(bin_to_int("111"))  # Ejercicio 5

# cumple()  # Ejercicio 6

edad_superior((10, 20, 32, 28, 17, 23, 11, 13, 16, 38), 20)  # Ejercicio 7

nombres = {"Angel", "Diego", "Lizbeth", "Ricardo", "Juan", "Jose", "Amelia", "Luis", "Santiago", "Maria"}  # Ejercicio 8
print(contar_nombres(nombres))

contar_vocales() # Ejercicio 9

print(is_bisiesto(2024))
print(is_bisiesto(2022))
'''
    Simulacion
    Redes de computadoras
    Fundamentos de inteligencia de negocios
    Lenguajes y automatas II
    Programacion web
    
    Gestion de proyectos de software
    Sistemas programables
'''
