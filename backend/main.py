from fastapi import FastAPI
from fastapi import Request
from routers import auth, documents
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Инициализация базы данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение маршрутов
app.include_router(auth.router)
app.include_router(documents.router)

# Монтируем статические файлы
#app.mount("/", StaticFiles(directory="./frontend/build", html=True), name="frontend")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Обрабатываем запрос: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Ответ: {response.status_code}")
    return response