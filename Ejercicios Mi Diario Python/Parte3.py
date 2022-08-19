''' Ejercicio 3
    Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
    las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
    últimas tiene que decir que riman un poco y si no, que no riman.
'''


def rimas(palabra1, palabra2):
    if palabra1[-3:].lower() == palabra2[-3:].lower():
        print("Las palabras riman")
    elif palabra1[-2:].lower() == palabra2[-2:].lower():
        print("Las palabras riman un poco")
    else:
        print("Las palabras no riman")


''' Ejercicio 4
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés 
y un numero de años. Muestra por pantalla en cuanto se habrá convertido el capital 
inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se 
convierte en C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una 
cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares 
al cabo de 20 años.'''


def inversion():
    cantidad = int(input("Ingrese una cantidad de dolares: "))
    tasa_interes = float(input("Ingresa la tasa de interes: "))
    years = int(input("A cuantos años? "))
    capital_final = cantidad * (1+tasa_interes/100)**years
    print("El capital final es ", capital_final)


rimas("iman", "gran")
inversion()
