from generadores import verificar_numero_cuenta

def es_numero(numero):
    try:
        numero_int = int(numero)
        return True
    except ValueError:
        return False


def es_numero_float(numero):
    try:
        numero_int = float(numero)
        return True
    except ValueError:
        return False


def ingresar_edad():
    while True:
        edad = input("-#-    Ingrese la edad: ")
        if es_numero(edad):

            if 18 <= int(edad) <= 26:
                return int(edad)
            else:
                print("-#-    Edad Invalida")
        else:
            print("-#-    Caracter Invalido")


def ingresar_semestre():
    while True:
        semestre = input("-#-    Ingrese el semestre: ")
        if es_numero(semestre):

            if 1 <= int(semestre) <= 9:
                return int(semestre)
            else:
                print("-#-    Semestre invalido")
        else:
            print("-#-    Caracter Invalido")


def ingresar_promedio():
    while True:
        promedio = input("-#-    Ingrese el promedio: ")
        if es_numero_float(promedio):

            if 5.0 <= float(promedio) <= 10.0:
                return float(promedio)
            else:
                print("-#-    Promedio Invalido")
        else:
            print("-#-    Caracter Invalido")


def ingresar_materias():
    materias = []
    for i in range(5):
        materia = input(f"Ingrese la materia numero {i + 1}: ")
        materias.append(materia)

    return materias


def ingresar_num_cuenta():
    numero = input("-#-    Ingrese el numero de cuenta: ")
    while not verificar_numero_cuenta(numero):
        print("-#-    Recuerde que el numero de cuenta es numerico de longitud 9")
        print("-#-    Y esta entre el rango de 314000000 a 324999999")
        numero = input("-#-    Ingrese nuevamente el numero de cuenta: ")

    return int(numero)
