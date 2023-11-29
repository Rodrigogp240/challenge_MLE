import fastapi

from pydantic import BaseModel
from typing import List
from .model import DelayModel

app = fastapi.FastAPI()
model = DelayModel()

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

    for flight_item in data.flights:
        prediction_result = model.predict(flight_item.OPERA, flight_item.TIPOVUELO, flight_item.MES)
        predictions.append({"prediction": prediction_result})

    return {"predictions": predictions}