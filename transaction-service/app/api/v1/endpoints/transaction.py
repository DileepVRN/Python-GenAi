from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.transaction import TransferRequest
from app.services.transaction_service import TransactionService
from app.db.session import SessionLocal
from app.core.security import verify_token

router = APIRouter()
service = TransactionService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transfer")
def transfer(
    data: TransferRequest,
    db: Session = Depends(get_db)
):
    return service.transfer(db, data)