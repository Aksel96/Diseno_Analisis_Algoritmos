import random

numeros_cuenta = set()


def gen_promedio():
    promedio = round(random.uniform(5, 10), 2)
    return promedio


def gen_edad():
    edad = random.randint(18, 26)
    return edad


def gen_semestre():
    semestre = random.randint(1, 9)
    return semestre


def gen_numero_cuenta():
    while True:
        numero_cuenta = f"{random.randint(316000000, 324999999)}"
        if numero_cuenta not in numeros_cuenta:
            numeros_cuenta.add(numero_cuenta)
            return int(numero_cuenta)


def verificar_numero_cuenta(numero):
    try:
        numero_int = int(numero)

        if 313999999 <= numero_int <= 324999999:
            if numero_int not in numeros_cuenta:
                numeros_cuenta.add(numero_int)
                return True
            else:
                print(f"El numero de cuenta \"{numero}\" ya existe")
                return False
        else:
            print(f"El numero \"{numero}\" no es un numero de cuenta valido")
            return False
    except ValueError:
        print(f"Caracter Invalido")
        return False


def verificar_numero_cuenta_correcto(numero):
    try:
        numero_int = int(numero)

        if 313999999 <= numero_int <= 324999999:
            return True
        else:
            print(f"El numero \"{numero}\" no es un numero de cuenta valido")
            return False
    except ValueError:
        print(f"Caracter Invalido")
        return False
