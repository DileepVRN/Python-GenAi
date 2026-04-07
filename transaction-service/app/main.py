from fastapi import FastAPI
from app.api.v1.endpoints.transaction import router as txn_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(txn_router, prefix="/transactions", tags=["Transactions"])