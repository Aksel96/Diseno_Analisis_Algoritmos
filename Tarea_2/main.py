# FES ARAGON
# ICO
# DISEÑO Y ANALISIS DE ALGORITMOS
# AKSEL VILLELA ANDRADE
# 15/08/2024

# Asignacion de la lista T(n) = 1, ya que la estamos definiendo desde un inicio, es decir tiene valores fijos
datos = [1, 2, 3]

repeticiones = 0  # Asignacion T(n) = 1

num_datos = len(datos)  # Calcular el tamaño del arreglo T(n) = 1, ya que el arreglo tiene un tamaño fijo

print(f"Entrada: {datos}")  # Impresion en pantalla T(n) = 1

for i in range(num_datos):  # Un bucle que depende de una varianle T(n) = n
    for j in range(num_datos):  # Bucle que depende de una variable T(n) = n
        print(datos[i], datos[j])  # Impresion en pantalla T(n) = 1
        repeticiones += 1  # Sumar un 1 a una variable T(n) = 1

print(f"Total repeticiones: {repeticiones}")  # Impresion en pantalla T(n) = 1

# Suma total de complejidad de este algoritmo:
# T(n) = 1 + 1 + 1 + 1 + ( n * n ) + 1 + 1 + 1
# Resultado: T(n) = n^2 + 7
