from pydantic import BaseModel

class CarInput(BaseModel):
    make:str
    model:str
    year:int
    engine:str
    cylinders:float
    fuel:str
    body:str
    drivetrain:str

class PricePrediction(BaseModel):
    predicted_price: float