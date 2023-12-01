import fastapi
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import List

app = fastapi.FastAPI()

class FlightItem(BaseModel):
    OPERA: str
    TIPOVUELO: str = Field(..., regex="^[IN]$", description="Allowed values are 'I' or 'N'")
    MES: int = Field(..., ge=1, le=12, description="Must be an integer between 1 and 12 (inclusive)")

class FlightData(BaseModel):
    flights: List[FlightItem]

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}

@app.post("/predict", status_code=200)
async def post_predict(data: FlightData) -> dict:
    try:
        return {"predict": [0]}
    except ValueError:
        raise HTTPException(status_code=400)
