import numpy as np


def generate_pacman_map():
    n = 1
    p = 0.5
    # El tamaño minimo debera ser 5 por los multiplos de los filtros,
    # el recomendado es 7 por la pantalla de implementación
    size = 7
    grid = np.random.binomial(n, p, size=(size, size))

    first_row = grid[0]
    first_row[first_row == 1] = 0
    grid[0] = first_row
    for i in range(1, size):
        grid[i, size-1] = 1

    def carve_maze(grid, size):
        output_grid = np.empty([size*3, size*3], dtype=str)
        output_grid[:] = 1
        i = 0
        j = 0
        while i < size:
            w = i*3 + 1
            while j < size:
                k = j*3 + 1
                toss = grid[i, j]
                output_grid[w, k] = 2
                if toss == 0 and k+2 < size*3:
                    output_grid[w, k+1] = 2
                    output_grid[w, k+2] = 2
                if toss == 1 and w-2 >= 0:
                    output_grid[w-1, k] = 2
                    output_grid[w-2, k] = 2
                j = j + 1
            i = i + 1
            j = 0
        return output_grid

    matriz = carve_maze(grid, size)  # min 5
    matriz = [[int(elemento) for elemento in fila] for fila in matriz.tolist()]

# Recorrido de matriz (mapa) opteniendo segmentos de igual dimension a los filtros evaluados.

    def LCM(matriz, filtros, start_y, start_x):
        for filtroPositio in filtros:
            filtro = filtroPositio[0]
            for y in range(start_y, len(matriz)-(len(filtro))+1):
                for x in range(start_x, len(matriz[y])-(len(filtro[0]))):
                    segment = []
                    for i in range(len(filtro)):
                        array = matriz[y+i][x:x+len(filtro[i])]
                        segment.append(array)
                    if areEquals(filtro, segment):
                        matriz[y+filtroPositio[1]][x +
                                                   filtroPositio[2]] = filtroPositio[3]
        matriz[-1] = [1 for elemento in matriz[-1]]
        return matriz

    filtros_SO = [
        ([
            [1, 1, 1],
            [1, 2, 1]
        ], 0, 1, 2),

        ([
            [1, 2, 1],
            [1, 1, 1]
        ], 1, 1, 2),

        ([
            [1, 1],
            [1, 2],
            [1, 1]
        ], 1, 0, 2),

        ([
            [1, 1],
            [2, 1],
            [1, 1]
        ], 1, 1, 2),

        ([
            [2, 1, 2],
            [2, 2, 2],
            [2, 1, 2]
        ], 1, 1, 1),

        ([
            [2, 2, 2],
            [1, 2, 1],
            [2, 2, 2]
        ], 1, 1, 1)
    ]

    filtros_CO = [
        ([
            [1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2]
        ], 0, 1, 2),

        ([
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 1]
        ], 0, 3, 2),

        ([
            [2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1]
        ], 1, 3, 2),

        ([
            [1, 2, 2, 2, 2],
            [1, 1, 1, 1, 1]
        ], 1, 1, 2),

        ([
            [1, 1],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2]
        ], 1, 0, 2),

        ([
            [1, 1],
            [2, 1],
            [2, 1],
            [2, 1],
            [2, 1]
        ], 1, 1, 2),

        ([
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 1]
        ], 3, 0, 2),

        ([
            [2, 1],
            [2, 1],
            [2, 1],
            [2, 1],
            [1, 1]
        ], 3, 1, 2)
    ]


# Compara que el filtro sea igual al segmento evaluado

    def areEquals(filter, segment):
        if filter == segment:
            return True
        else:
            return False

# Primero se aplica los filtros SO (Sin orillas), esto se indica por los parametros 1, 1
    matriz = LCM(matriz, filtros_SO, 1, 1)

# Despues se aplican los filtros CO (Con orillas), esto se indica por los parametros 0, 1
    matriz = LCM(matriz, filtros_CO, 0, 1)

    gosth_cel_start_y = int(len(matriz)/2)-1
    gosth_cel_start_x = int(len(matriz)/2)-2

    for y in range(4):
        for x in range(5):
            if y == 0:
                if x == 2:
                    matriz[gosth_cel_start_y+y][gosth_cel_start_x+x] = 3
                    count = 1
                    while matriz[gosth_cel_start_y+y-count][gosth_cel_start_x+x] == 1:
                        matriz[gosth_cel_start_y+y -
                               count][gosth_cel_start_x+x] = 2
                        count += 1
                else:
                    matriz[gosth_cel_start_y+y][gosth_cel_start_x+x] = 1
            elif y == 3:
                matriz[gosth_cel_start_y+y][gosth_cel_start_x+x] = 1
            else:
                if x == 0 or x == 4:
                    matriz[gosth_cel_start_y+y][gosth_cel_start_x+x] = 1
                else:
                    matriz[gosth_cel_start_y+y][gosth_cel_start_x+x] = 3

    return matriz
