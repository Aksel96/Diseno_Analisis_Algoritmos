pila = []


# En esta funcion leemos el laberinto desde un archivo csv y lo retornamos en una lista bidimencional
def leer_laberinto():
    with open('labe.csv', 'r') as archivo:
        laberinto = []

        for linea in archivo:
            fila = linea.strip().split(',')
            laberinto.append(fila)

    return laberinto


# Funcion para mostrar en pantalla el laberinto
def pintar_laberinto(laberinto):
    for i in range(len(laberinto)):
        print(f"{i} {laberinto[i]}")


# Funcion para verificar que un moviento sea valido (no salirse de los limites del laberinto y que no sea una pared "p")
def verificar_movimiento(laberinto, x, y):
    filas = len(laberinto)
    columnas = len(laberinto[0]) if filas > 0 else 0

    return 0 <= x < filas and 0 <= y < columnas and laberinto[x][y] != 'p'


# Funcion para moverse arriba, si es un movimiento valido entonces regresamos las coordenadas, pero en el eje x
# le quitamos 1 para moverlo una posicion hacia arriba
def mover_arriba(laberinto, x, y):
    if verificar_movimiento(laberinto, x - 1, y):
        return x - 1, y
    return None


# Funcion para moverse hacia abajo, se verifica el movimiento y regresamos las coodenadas pero le sumamos 1 al eje x
# para moverlo una posicion hacia abajo
def mover_abajo(laberinto, x, y):
    if verificar_movimiento(laberinto, x + 1, y):
        return x + 1, y
    return None


# Funcion para moverse hacia la izquierda, se verifica el movimiento y regresamos las coodenadas pero le restamos 1
#  al eje y para moverlo una posicion hacia la izquierda
def mover_izquierda(laberinto, x, y):
    if verificar_movimiento(laberinto, x, y - 1):
        return x, y - 1
    return None


# Funcion para moverse hacia la derecha, se verifica el movimiento y regresamos las coodenadas pero le sumamos 1
#  al eje y para moverlo una posicion hacia la derecha
def mover_derecha(laberinto, x, y):
    if verificar_movimiento(laberinto, x, y + 1):
        return x, y + 1
    return None


# Funcion para buscar en donde se encuentra la entrada del laberinto, retornamos las coordenadas de la entrada
def buscar_entrada(laberinto, entrada):
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if laberinto[x][y] == entrada:
                return x, y
    return None


def main():
    laberinto = leer_laberinto()  # -> 1)
    laberinto_ori = leer_laberinto()
    coor_x_entrada, coor_y_entrada = buscar_entrada(laberinto, 'E')  # -> 2)

    if coor_x_entrada is None or coor_y_entrada is None:  # -> 3)
        print("El laberinto no tiene una entrada")
        return

    pila.append((coor_x_entrada, coor_y_entrada))  # -> 4)

    laberinto[coor_x_entrada][coor_y_entrada] = 'y'  # -> 5)

    solucion_encontrada = False  # -> 6)

    num_movimientos = 0  # -> 7)

    while pila and not solucion_encontrada:  # -> 8)
        num_movimientos += 1  # -> 9)

        x, y = pila[-1]  # -> 10)

        nueva_posicion = mover_izquierda(laberinto, x, y)  # -> 11)
        if nueva_posicion:  # -> 12)
            nueva_x, nueva_y = nueva_posicion
            if laberinto[nueva_x][nueva_y] == 's':
                laberinto[nueva_x][nueva_y] = 'O'
                solucion_encontrada = True
            elif laberinto[nueva_x][nueva_y] == 'c':
                laberinto[nueva_x][nueva_y] = 'y'
                pila.append((nueva_x, nueva_y))
                continue

        nueva_posicion = mover_arriba(laberinto, x, y)  # -> 13)
        if nueva_posicion:  # -> 14)
            nueva_x, nueva_y = nueva_posicion
            if laberinto[nueva_x][nueva_y] == 's':
                laberinto[nueva_x][nueva_y] = 'O'
                solucion_encontrada = True
            elif laberinto[nueva_x][nueva_y] == 'c':
                laberinto[nueva_x][nueva_y] = 'y'
                pila.append((nueva_x, nueva_y))
                continue

        nueva_posicion = mover_derecha(laberinto, x, y)  # -> 15)
        if nueva_posicion:  # -> 16)
            nueva_x, nueva_y = nueva_posicion
            if laberinto[nueva_x][nueva_y] == 's':
                laberinto[nueva_x][nueva_y] = 'O'
                solucion_encontrada = True
            elif laberinto[nueva_x][nueva_y] == 'c':
                laberinto[nueva_x][nueva_y] = 'y'
                pila.append((nueva_x, nueva_y))
                continue

        nueva_posicion = mover_abajo(laberinto, x, y)  # -> 17)
        if nueva_posicion:  # -> 18)
            nueva_x, nueva_y = nueva_posicion
            if laberinto[nueva_x][nueva_y] == 's':
                laberinto[nueva_x][nueva_y] = 'O'
                solucion_encontrada = True

            elif laberinto[nueva_x][nueva_y] == 'c':
                laberinto[nueva_x][nueva_y] = 'y'
                pila.append((nueva_x, nueva_y))
                continue
        if not solucion_encontrada:  # -> 19)
            laberinto[x][y] = 'x'
            pila.pop()

    print("Laberinto Original:")
    pintar_laberinto(laberinto_ori)

    if solucion_encontrada:  # -> 20)
        print(f"Se encontro una solucion con un total de {num_movimientos} movimientos:")
    else:
        print("No se encontro ninguna solucion")

    pintar_laberinto(laberinto)


if __name__ == "__main__":
    main()
