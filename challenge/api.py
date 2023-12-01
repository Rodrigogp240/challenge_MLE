import fastapi
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List

app = fastapi.FastAPI()


class FlightItem(BaseModel):
    OPERA: str
    TIPOVUELO: str = Field(..., regex="^[IN]$", description="Allowed values are 'I' or 'N'")
    MES: int = Field(..., ge=1, le=12, description="Must be an integer between 1 and 12 (inclusive)")

class FlightData(BaseModel):
    flights: List[FlightItem]

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": "Validation error", "errors": exc.errors()},
    )

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}

@app.post("/predict", status_code=200)
async def post_predict(data: FlightData) -> dict:
    data
    return {"predict": [0]}


