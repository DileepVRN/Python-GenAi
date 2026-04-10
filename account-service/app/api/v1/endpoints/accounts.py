from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.account import AccountCreate
from app.services.account_service import AccountService
from app.db.session import SessionLocal

# ✅ Router must be defined
router = APIRouter()

# Service instance
service = AccountService()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create account
@router.post("/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    print("inside accounts",account)
    return service.create_account(db, account)

# Get all accounts
@router.get("/")
def get_accounts(db: Session = Depends(get_db)):
    return service.get_accounts(db)