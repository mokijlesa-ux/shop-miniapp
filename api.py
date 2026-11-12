from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import aiosqlite  # Пока отключим базу данных
# from config import DB_PATH

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
    # Временно возвращаем тестовые товары, чтобы проверить работу сайта в Telegram
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