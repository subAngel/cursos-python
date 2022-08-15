# For es para listas, tuplas y diccionarios

semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

# Ejemplo de FOR con listas
# for dia in semana:    # dia es la variable de control
#     print(dia)

# Ejemplo de FOR con break
'''
for x in semana:
    print(x)
    if x == 'Viernes':
        break
'''

# Ejemplo de FOR con excepcion
'''
for dia in semana:
    if dia == "Viernes":
        break
    print(dia)
'''

# Ejemplo de FOR con repeticion
numero = 5
for n in range(numero):
    print("Hola")