# Escribir una función reciba un diccionario con las asignaturas y
# las notas de un alumno y devuelva otro diccionario con las asignaturas
# en mayúsculas y las calificaciones correspondientes a las notas aprobadas.


def calif(puntuacion):
    if puntuacion <7:
        return 'Reprobado'
    elif 7 <= puntuacion < 10:
        return 'Aprobado'
    elif puntuacion == 10:
        return 'Excelente'
    else:
        return 'NA'


# funcion que recibe una tupla con una asignatura y su nota
def materia_aprobada(materia):
    return (materia[1] >= 7)


def aplicar_calif(puntuaciones): # {'matematicas': 5, 'espanol':8}
    aprobada = dict(filter(materia_aprobada, puntuaciones.items()))
    materia = map(str.upper, aprobada.keys())
    calificacion = map(calif, aprobada.values())
    return dict(zip(materia, calificacion))


print(aplicar_calif({'matematicas':10, 'Historia':8, 'Geografia':4}))
