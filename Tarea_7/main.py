def producto_mas_alto(arreglo):
    maximo = 0  # -> 1)
    indice_i = None  # -> 2)
    indice_j = None  # -> 3)
    n = len(arreglo)  # -> 4)
    for i in range(n):  # -> 5)
        for j in range(n):  # -> 6)
            if i != j:  # -> 7)
                a = arreglo[i] * arreglo[j]  # -> 8)
                if a > maximo:  # -> 9)
                    indice_i = i  # -> 10)
                    indice_j = j  # -> 11)
                    maximo = a  # -> 12)

    return maximo, indice_i, indice_j  # -> 13)


def encontrar_patron(array, patron):
    tamanio_array = len(array)  # -> 1)
    tamanio_patron = len(patron)  # -> 2)
    contador = 0  # -> 3)
    for i in range((tamanio_array - tamanio_patron) + 1):  # -> 4)
        for j in range(tamanio_patron):  # -> 5)
            if array[i + j] == patron[j]:  # -> 6)
                contador += 1  # -> 7)
                if contador == tamanio_patron:  # -> 8)
                    return True  # -> 9)
            else:
                contador = 0  # -> 10)
                break  # -> 11)
    return False  # -> 12)


def descifrar_cesar(texto_sf):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"  # -> 1)
    tamano_alfa = len(alfabeto)  # -> 2)
    texto_se = texto_sf.replace(" ", "")  # -> 3)
    texto = texto_se.lower()  # -> 4)
    tamano_texto = len(texto)  # -> 5)
    for i in range(tamano_alfa):  # -> 6)
        cadena = ""  # -> 7)
        for j in range(tamano_texto):  # -> 8)
            pos = alfabeto.index(texto[j])  # -> 9)
            cadena += alfabeto[(pos + i) % tamano_alfa]  # -> 10)
        print(f"Intento numero {i}: {cadena}")  # -> 11)


def main():
    # Ejercicio numero 1

    print("######################################################")

    arreglo = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

    maximo, i, j = producto_mas_alto(arreglo)

    print(f"Arreglo: {arreglo}")
    print(f"El mayor producto posible es [{maximo}] con los numeros {arreglo[i]} y {arreglo[j]}")

    print("######################################################\n")

    # Ejercicio numero 2

    print("######################################################")

    array = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    patron = [0, 1, 1, 0, 1]

    verificar = encontrar_patron(array, patron)

    print(f"Arreglo: {array}")
    print(f"Patron a buscar: {patron}")

    if verificar:
        print("---> [SI] se encontro el patron en el arreglo")
    else:
        print("[NO] se encontro el patron a buscar")

    print("######################################################\n")

    # Ejercicio numero 3

    print("######################################################\n")

    texto = "cqrccqslrcvrnagdpybn"

    print(f"Texto a buscar: {texto}")

    descifrar_cesar(texto)

    print("######################################################")


if __name__ == '__main__':
    main()
