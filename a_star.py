import numpy as np


class Nodo:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Costo desde el inicio hasta este nodo
        self.h = 0  # Heurística (estimación de costo restante)
        self.f = 0  # Costo total (f = g + h)


def heuristica_manhattan(nodo_actual, nodo_final):
    return abs(nodo_actual.x - nodo_final.x) + abs(nodo_actual.y - nodo_final.y)


def a_estrella(mapa, inicio, final):
    movimientos = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    abierta = []  # Lista ordenada de nodos abiertos

    nodo_inicio = Nodo(inicio[0], inicio[1])
    nodo_final = Nodo(final[0], final[1])

    abierta.append(nodo_inicio)

    while abierta:
        # Ordenar la lista de nodos abiertos por su costo total f
        abierta.sort(key=lambda x: x.f)
        nodo_actual = abierta.pop(0)  # Tomar el nodo con menor costo f

        if nodo_actual.x == nodo_final.x and nodo_actual.y == nodo_final.y:
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.parent
            return camino[::-1]

        for dx, dy in movimientos:
            x_vecino, y_vecino = nodo_actual.x + dx, nodo_actual.y + dy

            if 0 <= x_vecino < mapa.shape[0] and 0 <= y_vecino < mapa.shape[1] and mapa[x_vecino, y_vecino] == 0:
                vecino = Nodo(x_vecino, y_vecino, nodo_actual)
                vecino.g = nodo_actual.g + 1
                vecino.h = heuristica_manhattan(vecino, nodo_final)
                vecino.f = vecino.g + vecino.h

                # Verificar si el vecino ya está en la lista de nodos abiertos
                encontrado = False
                for nodo_abierto in abierta:
                    if nodo_abierto.x == vecino.x and nodo_abierto.y == vecino.y:
                        encontrado = True
                        if vecino.f < nodo_abierto.f:
                            nodo_abierto.parent = vecino.parent
                            nodo_abierto.g = vecino.g
                            nodo_abierto.h = vecino.h
                            nodo_abierto.f = vecino.f
                            break

                if not encontrado:
                    abierta.append(vecino)

    return None
