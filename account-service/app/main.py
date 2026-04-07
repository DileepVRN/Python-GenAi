from fastapi import FastAPI
from app.api.endpoints.v1 import accounts
from app.api.endpoints.v1.accounts import router as account_router
from app.db.base import Base
from app.db.session import engine
app = FastAPI(title="account-service")


# Create tables
Base.metadata.create_all(bind=engine)
app.include_router(account_router, prefix="/accounts", tags=["Accounts"])