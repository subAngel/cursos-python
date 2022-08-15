# Escribir una función reciba un diccionario con las asignaturas y
# las notas de un alumno y devuelva otro diccionario con las asignaturas
# en mayúsculas y las calificaciones correspondientes a las notas.

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
    for x in puntuaciones.values():
        if x >= 7:
            asignatura = map(str.upper, puntuaciones.keys())
            calificacion = map(calif, puntuaciones.values())
    return dict(zip(asignatura, calificacion))


print(aplicar_calif({'matematicas':10, 'Historia':8, 'Geografia':4}))
