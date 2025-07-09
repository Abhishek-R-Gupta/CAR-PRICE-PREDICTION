from fastapi import APIRouter
from app.schemas import CarInput, PricePrediction
from app.model import predict_price

router = APIRouter()

@router.post("/predict",response_model = PricePrediction)
def predict(data: CarInput):
    result = predict_price(data)
    return {"predicted_price":result}

@router.get('/')
def home():
    return {"message":"hello user welcome to car price prediction page"}


