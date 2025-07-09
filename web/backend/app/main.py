from fastapi import FastAPI
from app.routes import router

app = FastAPI(title='Car Price Prediction API')

app.include_router(router)