from fastapi import APIRouter, Depends
import httpx
from app.core.config import settings
from app.core.security import verify_token

router = APIRouter()

@router.post("/transfer")
async def transfer(data: dict, user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.TRANSACTION_SERVICE}/transactions/transfer",
            json=data
        )
        return response.json()