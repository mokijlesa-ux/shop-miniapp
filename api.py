from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
async def get_products():
    # Тестовые товары, чтобы сайт работал прямо сейчас
    return [
        {
            "id": 1,
            "name": "Тестовый Под Waka",
            "description": "Отличный вкус",
            "price": 1200,
            "image": "https://via.placeholder.com/150x150/2a2a35/ffffff?text=Pod"
        },
        {
            "id": 2,
            "name": "Жидкость Манго",
            "description": "20мг",
            "price": 350,
            "image": "https://via.placeholder.com/150x150/2a2a35/ffffff?text=Liquid"
        }
    ]