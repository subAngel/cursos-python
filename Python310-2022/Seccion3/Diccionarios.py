# Diccionarios en python
nombres = {1:'Angel', 2:'Jesus', 3:2.5, 4:False, 5:True}
# print(nombres)
# La duplicidad no esta permitida en los diccinoarios

tupla = {"nombre": 'Angel', "edad":21, "tupla":(1,2,True,"Adios")}
# print(tupla)
# print(len(tupla))

# Acceder a los valores de un diccionario, keys(), values(), items()
print(nombres[2])   # --> peor
x = nombres[2]      # --> Mejor
print(x)

print(nombres.keys())
print(nombres.values())
print(nombres.items())

# Cambiar elemenots con update
nombres[2] = 'Angel'
print(nombres)

nombres.update({2:'Luis'})
print(nombres)

# Eliminar una lista,
print(nombres)
nombres.pop(1)
print(nombres)
nombres.popitem()   # elimina el ultimo item
print(nombres)
