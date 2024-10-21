def mochila(pesos, valores, capacidad, indice):
    if indice == 0 or capacidad == 0:  # -> 1)
        return 0

    if pesos[indice - 1] > capacidad:  # -> 2)
        return mochila(pesos, valores, capacidad, indice - 1)

    opcion_1 = mochila(pesos, valores, capacidad, indice - 1)  # -> 3)

    opcion_2 = valores[indice - 1] + mochila(pesos, valores, capacidad - pesos[indice - 1], indice - 1)  # -> 4)

    if opcion_2 > opcion_1:  # -> 5)
        return opcion_2
    else:
        return opcion_1


def main():
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 8]
    capacidad = 8
    indice = len(pesos)

    maximo = mochila(pesos, valores, capacidad, indice)
    print(f"Pesos : {pesos}")
    print(f"Valores : {valores}")
    print(f"El valor maximo que se puede obtener es: {maximo} ")


if __name__ == '__main__':
    main()
