def http_error(status=0):
    match status:
        case 400:
            return "Solicitud incorrecta"
        case 404:
            return "No encontrada"
        case 408:
            return "hola, me llamo angel"
        case _: # caso por defecto
            return "adios"


print(http_error())