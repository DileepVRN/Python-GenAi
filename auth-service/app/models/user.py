"""
User Database Model
Defines the User table schema and ORM mapping for SQLAlchemy.
Represents user accounts in the authentication system.
"""
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    """
    SQLAlchemy ORM model for the User entity.
    Maps to 'users' table in the database.
    Stores user authentication credentials.
    """
    # Table name in database
    __tablename__ = "users"

    # Primary key - auto-incremented integer ID
    # index=True creates database index for faster lookups
    id = Column(Integer, primary_key=True, index=True)
    
    # Username field - must be unique across all users
    # unique=True: Database enforces uniqueness constraint
    # index=True: Creates index for fast username lookups during login
    # String(50): VARCHAR(50) in database
    username = Column(String(50), unique=True, index=True)
    
    # Password field - stores HASHED password (NEVER plain text!)
    # String(200): Hashed passwords need more space than plain passwords
    # Must be hashed using bcrypt or similar before storing
    password = Column(String(200))