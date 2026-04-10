from fastapi import APIRouter
import httpx
from app.core.config import settings

router = APIRouter()

@router.post("/login")
async def login(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.AUTH_SERVICE}/auth/login",
            json=data
        )
        return response.json()
    
@router.post("/register")
async def login(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.AUTH_SERVICE}/auth/register",
            json=data
        )
        return response.json()