from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import aiosqlite
from config import DB_PATH

app = FastAPI()

# Разрешаем вашему сайту на GitHub делать запросы к этому API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешаем всем (для теста). Позже можно заменить на "https://mokijlesa-ux.github.io"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
async def get_products():
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        # Берем только те товары, которые не скрыты (is_active = 1)
        cursor = await db.execute(
            "SELECT id, name, description, price, photo_file_id FROM products WHERE is_active = 1"
        )
        products = await cursor.fetchall()
        
        result = []
        for p in products:
            # Если фото нет, ставим красивую заглушку
            image_url = "https://via.placeholder.com/150x150/1c1c24/8b5cf6?text=VCATS" 
            
            # ВАЖНО: Чтобы отображать реальные фото из Telegram, 
            # боту нужно сначала получить прямую ссылку на файл через getFile. 
            # Пока оставим заглушку, чтобы не усложнять код.
            
            result.append({
                "id": p["id"],
                "name": p["name"],
                "description": p["description"],
                "price": p["price"],
                "image": image_url
            })
        return result