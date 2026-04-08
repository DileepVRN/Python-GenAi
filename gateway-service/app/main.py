from fastapi import FastAPI
from app.routes import auth, account, transaction

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(account.router, prefix="/accounts", tags=["Accounts"])
app.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])