from contextlib import asynccontextmanager

from app.db.base import Base
from app.db.session import engine
from fastapi import FastAPI
from app.api.v1.endpoints.accounts import router as account_router
from app.core.kafka_consumer import consume_transactions
import httpx
import asyncio 
import threading


# -------- AUTH CALL --------
async def call_auth_service(retries=3, delay=2): 
    for attempt in range(retries): 
        try: 
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://auth-service:8001/health", 
                    timeout=5.0
                ) 
                return response.json() 
        except Exception as e: 
            print(f"Attempt {attempt+1} failed: {e}") 
            await asyncio.sleep(delay) 
    return {"status": "down after retries"}

# -------- LIFESPAN --------
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔥 LIFESPAN TRIGGERED", flush=True)

    # Create database tables
    Base.metadata.create_all(bind=engine)

    thread = threading.Thread(target=consume_transactions, daemon=True)
    thread.start()

    result = await call_auth_service()
    print("Auth service status:", result)

    yield

    print("🛑 Shutdown...")

# -------- APP --------
app = FastAPI(title="account-service", lifespan=lifespan)

# ✅ ADD ROUTER HERE
app.include_router(
    account_router,
    prefix="/accounts",
    tags=["Accounts"]
)