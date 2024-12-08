from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from pydantic import BaseModel
from jose import JWTError, jwt
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


router = APIRouter()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

class UserCredentials(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    logger.info(f"Получен токен: {token}")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        logger.info(f"ID пользователя из токена: {user_id}")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        logger.info(f"Найден пользователь: {user.username}")
        return user
    except JWTError as e:
        logger.error(f"Ошибка токена: {e}")
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/api/login", response_model=Token)
def login(credentials: UserCredentials, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = create_access_token({"sub": str(user.id)})
    print("login success")
    return {"access_token": token, "token_type": "bearer"}
