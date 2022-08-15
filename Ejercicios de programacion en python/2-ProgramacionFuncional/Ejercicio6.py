# Escribir una funcion que reciba una lista de notas y devuelva la lista de calificaciones
# correspondientes a esas notas


def calificacion(nota):
    if nota < 7:
        return 'Reprobado'
    elif 7 <= nota < 10:
        return 'Aprobado'
    elif nota == 10:
        return 'Excelente'
    else:
        return 'NA'


def aplicar_calif(notas):
    return list(map(calificacion, notas))


print(aplicar_calif([4, 6.7, 7, 4, 9, 7, 10, 10]))
