"""
Account Service Main Application
FastAPI application entry point for the Account Microservice.
Initializes the application and configures routes.
"""
import threading
from app.core.kafka_consumer import consume_transactions
from fastapi import FastAPI
from app.api.endpoints.v1.accounts import router as account_router
from app.db.base import Base
from app.db.session import engine

# ========== APPLICATION INITIALIZATION ==========
# Create FastAPI application instance
# title: Displayed in Swagger API documentation
app = FastAPI(title="account-service")

# ========== DATABASE INITIALIZATION ==========
# Create all database tables defined in ORM models
# Uses SQLAlchemy metadata to generate CREATE TABLE statements
# Safe to call multiple times (tables only created if they don't exist)
Base.metadata.create_all(bind=engine)

# ========== ROUTE REGISTRATION ==========
# Include account routes to the application
# prefix="/accounts": All routes prefixed with /accounts
# tags=["Accounts"]: Groups endpoints in Swagger documentation
# Example: POST /accounts/ for create_account endpoint
app.include_router(account_router, prefix="/accounts", tags=["Accounts"])



@app.on_event("startup")
def start_kafka():
    thread = threading.Thread(target=consume_transactions)
    thread.start()