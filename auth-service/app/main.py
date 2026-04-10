"""
Auth Service Main Application
FastAPI application entry point for the Authentication Microservice.
Initializes the application, configures database, and registers routes.
"""
from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router
from app.db.base import Base
from app.db.session import engine
from app.models.user import User

# ========== APPLICATION INITIALIZATION ==========
# Create FastAPI application instance
# This is the main ASGI application that receives HTTP requests
app = FastAPI()

# ========== STARTUP EVENT ==========
@app.on_event("startup")
def startup():
    """
    Application startup hook.
    FastAPI automatically calls this when the application starts.
    
    Operations:
    1. Initialize database tables from ORM models
    2. Verify database connectivity
    3. Prepare application for handling requests
    
    Called once when:
    - Development server starts: uvicorn app.main:app --reload
    - Production server starts
    - Application is reloaded
    """
    # Create all database tables defined in ORM models
    # Uses SQLAlchemy metadata to generate CREATE TABLE statements
    # Safe to call multiple times (tables only created if they don't exist)
    # If tables already exist, this operation is a no-op
    Base.metadata.create_all(bind=engine)

# ========== ROUTE REGISTRATION ==========
# Include authentication routes to the application
# prefix="/auth": All routes prefixed with /auth
# tags=["Auth"]: Groups endpoints in Swagger documentation
# Example routes:
#   - POST /auth/register - Register new user
#   - POST /auth/login - Authenticate user and get token
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/health")
def health():
    return {"status": "up"}