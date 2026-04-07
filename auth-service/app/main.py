from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router
from app.db.base import Base
from app.db.session import engine
from app.models.user import User

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])