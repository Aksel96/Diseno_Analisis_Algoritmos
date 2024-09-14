def busqueda_lineal(lista, dato):
    n = len(lista)  # -> 1)
    i = 0  # -> 2)

    while i < n and dato != lista[i]:  # -> 3)
        i += 1

    if n == i:  # -> 4)
        return -1
    else:
        return i


def busqueda_lineal_centinela(lista, dato):
    ultimo_tmp = lista[-1]  # -> 1)
    lista[-1] = dato  # -> 2)
    i = 0  # -> 3)

    while lista[i] != dato:  # -> 4)
        i += 1

    lista[-1] = ultimo_tmp  # -> 5)

    if i < len(lista) - 1 or lista[-1] == dato:  # -> 6
        return i
    else:
        return -1


def busqueda_binaria(lista, dato, inicio, fin):
    if inicio > fin:  # -> 1)
        return -1

    mid = inicio + (fin - inicio) // 2  # -> 2)

    if lista[mid] == dato:  # -> 3)
        return mid
    elif dato < lista[mid]:
        return busqueda_binaria(lista, dato, inicio, mid - 1)  # -> 4
    else:
        return busqueda_binaria(lista, dato, mid + 1, fin)  # -> 5


def main():
    # Busqueda Lineal
    lista_no_ord = [3, 2, 7, 5, 9]

    dato_a_buscar = 5

    resultado_lineal = busqueda_lineal(lista_no_ord, dato_a_buscar)

    print("-----    Busqueda Lineal    -----")

    print(f"Lista: {lista_no_ord} , Dato a buscar: {dato_a_buscar}")

    if resultado_lineal != -1:
        print(f"Se encontro el dato {dato_a_buscar} en el inidice: {resultado_lineal}")
    else:
        print(f"No se encontro el dato {dato_a_buscar} en la lista")

    # Busqueda Lineal con Centinela
    lista_centinela = [4, 2, 6, 9, 1, 8]

    dato_bus_cent = 8

    print("\n-----    Busqueda Lineal con Centinela    -----")

    print(f" Lista: {lista_centinela} , Dato a buscar: {dato_bus_cent}")

    resultado_centinela = busqueda_lineal_centinela(lista_centinela, dato_bus_cent)

    if resultado_centinela != -1:
        print(f"Se encontro el dato {dato_bus_cent} en el inidice: {resultado_centinela}")
    else:
        print(f"No se encontro el dato {dato_bus_cent} en la lista")

    # Busqueda Binaria
    lista_ord = [1, 2, 4, 5, 6, 7, 8, 9]

    print("\n-----    Busqueda Binaria    -----")

    dato_bus_bin = 7

    resultado_binaria = busqueda_binaria(lista_ord, dato_bus_bin, 0, len(lista_ord) - 1)

    print(f"Lista: {lista_ord} , Dato a buscar: {dato_bus_bin}")

    if resultado_binaria != -1:
        print(f"Se encontro el dato {dato_bus_bin} en el inidice: {resultado_binaria}")
    else:
        print(f"No se encontro el dato {dato_bus_bin} en la lista")


if __name__ == '__main__':
    main()
