from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.auth_service import AuthService
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserLogin
router = APIRouter()
service = AuthService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return service.register(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return service.login(db, user)