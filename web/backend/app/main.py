from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
# from streamlit.web.server import allow_cross_origin_requests

app = FastAPI(title='Car Price Prediction API')

origins =  ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

app.include_router(router)