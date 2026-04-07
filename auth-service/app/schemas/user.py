"""
User Pydantic Schemas
Defines request/response validation schemas for authentication endpoints.
Separates API contracts from database models.
"""
from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    Request schema for user registration endpoint.
    Validates registration input data from API clients.
    - username: Unique identifier for the user (required)
    - password: Plain text password (required) - will be hashed before storage
    """
    username: str
    password: str

class UserLogin(BaseModel):
    """
    Request schema for user login endpoint.
    Validates login credentials from API clients.
    - username: User's unique identifier (required)
    - password: Plain text password to verify (required) - compared against hashed password in DB
    """
    username: str
    password: str