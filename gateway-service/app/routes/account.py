from fastapi import APIRouter, Depends
import httpx
from app.core.config import settings
from app.core.security import verify_token

router = APIRouter()

@router.get("/")
async def get_accounts(user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.ACCOUNT_SERVICE}/accounts/")
        return response.json()

@router.post("/")
async def post_accounts(data: dict,user=Depends(verify_token)):
    print("inside gateway",data)
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.ACCOUNT_SERVICE}/accounts/",
             json=data
            )
        return response.json()