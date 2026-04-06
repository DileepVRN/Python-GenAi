from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="Banking GenAI Assistant",
    description="AI-powered banking assistant",
    version="1.0.0"
)

# Health check
@app.get("/")
def home():
    return {"message": "Banking GenAI Service Running 🚀"}
    
app.include_router(chat_router, prefix="/api")

# Include routes
app.include_router(chat_router, prefix="/api")