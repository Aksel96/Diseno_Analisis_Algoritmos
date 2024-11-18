import heapq


def leer_laberinto():
    with open('labe.csv', 'r') as archivo:
        laberinto = []
        for linea in archivo:
            fila = linea.strip().split(',')
            laberinto.append(fila)
    return laberinto


def pintar_laberinto(laberinto):
    for i, fila in enumerate(laberinto):
        print(f"{i:2d} {fila}")


def verificar_movimiento(laberinto, x, y):
    filas = len(laberinto)
    columnas = len(laberinto[0]) if filas > 0 else 0
    return 0 <= x < filas and 0 <= y < columnas and laberinto[x][y] != 'p'


def buscar_entrada(laberinto, entrada, salida):
    entrada_x_y = None
    salida_x_y = None
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if laberinto[x][y] == entrada:
                entrada_x_y = [x, y]
            if laberinto[x][y] == salida:
                salida_x_y = [x, y]
    return entrada_x_y, salida_x_y


def distancia_manhattan(actual, objetivo):
    return abs(actual[0] - objetivo[0]) + abs(actual[1] - objetivo[1])


def main():
    laberinto = leer_laberinto()  # -> 1)
    entrada, salida = buscar_entrada(laberinto, 'E', 's')  # -> 2)
    if entrada is None or salida is None:  # -> 3)
        print("El laberinto no tiene una entrada o salida válidas")
        return
    print("Laberinto original:")  # -> 4)
    pintar_laberinto(laberinto)  # -> 5)

    cola_prioridad = []  # -> 6)
    heapq.heappush(cola_prioridad, (0, entrada[0], entrada[1]))  # -> 7)
    visitados = set()  # -> 8)
    visitados.add((entrada[0], entrada[1]))  # -> 9)
    laberinto[entrada[0]][entrada[1]] = "Y"  # -> 10)

    solucion_encontrada = False  # -> 11)

    num_movimientos = 0  # -> 12)

    while cola_prioridad and not solucion_encontrada:  # -> 13)
        _, x, y = heapq.heappop(cola_prioridad)  # -> 14)

        if [x, y] == salida:  # -> 15)
            laberinto[x][y] = 'O'
            solucion_encontrada = True
            break

        movimientos = [  # -> 16)
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        for mov_x, mov_y in movimientos:  # -> 17)
            if verificar_movimiento(laberinto, mov_x, mov_y) and (mov_x, mov_y) not in visitados:  # -> 18)
                prioridad = distancia_manhattan((mov_x, mov_y), salida)  # -> 19)
                heapq.heappush(cola_prioridad, (prioridad, mov_x, mov_y))  # -> 20)
                visitados.add((mov_x, mov_y))  # -> 21)
                laberinto[mov_x][mov_y] = "Y"  # -> 22)
                num_movimientos += 1  # -> 23)

    if solucion_encontrada:  # -> 24)
        print("Solución encontrada:")
        pintar_laberinto(laberinto)
        print(f"Numero de movimientos : {num_movimientos}")
    else:
        print("No se encontró solución.")


if __name__ == '__main__':
    main()
