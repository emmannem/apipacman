from pydantic import BaseModel
from typing import List, Tuple


class MapaRequest(BaseModel):
    mapa: list[list[int]]
    inicio: tuple[int, int]
    final: tuple[int, int]


class MapaResponse(BaseModel):
    camino: list[tuple[int, int]]
