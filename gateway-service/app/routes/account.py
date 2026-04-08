from fastapi import APIRouter, Depends
import httpx
from app.core.config import settings
from app.core.security import verify_token

router = APIRouter()

@router.get("/")
async def get_accounts(user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.ACCOUNT_SERVICE}/accounts")
        return response.json()