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
