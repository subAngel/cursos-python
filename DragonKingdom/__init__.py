# Reino del Dragon....
import random
import time


def introduccion():
    texto =  '''+-------------------------------------------------------------------------------+
|       Estamos en una tierra llena de dragones. Delante de nuestr,             |
|       se ven dos cuevas. En una cueva, el dragon es amigable                  |
|       y compartira el tesoro contigo. El otro dragon                          |
|       es codicioso y hambriento, y te va a comer ni bien te vea.              |
+-------------------------------------------------------------------------------+'''
    print(texto, end='\n')


def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print("-> A que cueva quieres entrar? 1 o 2? ")
        cueva = input()

    return cueva


def cheqcueva(CambiarCueva):
    print("\tTe acercas a la Cueva...")
    time.sleep(2)
    print("\tEsta oscuro y tenebroso...")
    time.sleep(2)
    print("\tUn gran dragon salta delante tuyo, abre su boca y...")
    print("")
    time.sleep(2)

    FriendlyCueva = random.randint(1, 2)

    if CambiarCueva == str(FriendlyCueva):
        print("Te entrega el tesoro...")
    else:
        print("El dragon te come de un bocado....")


EmpezarNuevo = ("si")

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
    introduccion()

    NumCaverna = CambiarCueva()

    cheqcueva(NumCaverna)

    print("Quieres jugar de nuevo? (si o no)")
    EmpezarNuevo = input()












'''
 8 9 .... Gestion de proyectos, programacion Web
 17 18 .... Programacion logica funcional
'''