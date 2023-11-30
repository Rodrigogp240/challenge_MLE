import fastapi

from pydantic import BaseModel
from typing import List


app = fastapi.FastAPI()


class FlightItem(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int

class FlightData(BaseModel):
    flights: List[FlightItem]

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

@app.post("/predict", status_code=200)
async def post_predict(data: FlightData) -> dict:
    predictions = []
    return {"predictions": predictions}