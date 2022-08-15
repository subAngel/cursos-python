# Como usar las tuplas
# lista de varios tipos
nombres = ("Angel", "Lizbeth", 'Jesus', "Luz")
numeros = (4, 2, 1, 5)
valor   = (True, False, True)
comb    = ("Angel", 4, 3, False)

#print(comb)

# Acceder a elementos de una tupla
#print(nombres[2])

# Actualizar una tupla

# x = list(nombres)
# x[1] = "Jesus"
# nombres = tuple(x)
# print(nombres)

# Desempaquetar tupla

(uno,dos,tres,cuatro) = numeros
# print(uno)

# Metodos de una tupla: count(), index()
print(numeros.count(1))
print(numeros.index(5))