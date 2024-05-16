from fastapi import FastAPI, HTTPException
from schemas import MapaRequest, MapaResponse
from a_star import a_estrella
import numpy as np

app = FastAPI()


@app.post("/a-star/")
async def encontrar_camino(mapa_req: MapaRequest) -> MapaResponse:
    mapa = np.array(mapa_req.mapa)
    inicio = mapa_req.inicio
    final = mapa_req.final

    camino = a_estrella(mapa, inicio, final)

    if not camino:
        raise HTTPException(
            status_code=404, detail="No se encontró un camino válido.")

    return {"camino": camino}