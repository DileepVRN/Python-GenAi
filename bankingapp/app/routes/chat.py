from fastapi import APIRouter
from app.services.rag_service import rag_chat

router = APIRouter()


@router.post("/chat")
def chat(query: str):
    response = rag_chat(query)
    return {"response": response}