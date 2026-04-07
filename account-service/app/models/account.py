"""
Account Database Model
Defines the Account table schema and ORM mapping for SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base   # IMPORTANT: Must inherit from Base for ORM mapping

class Account(Base):
    """
    SQLAlchemy ORM model for the Account entity.
    Maps to 'accounts' table in the database.
    """
    # Table name in database
    __tablename__ = "accounts"

    # Primary key - auto-incremented integer ID
    # index=True creates database index for faster queries
    id = Column(Integer, primary_key=True, index=True)
    
    # Account holder's name - VARCHAR(100)
    name = Column(String(100))
    
    # Account balance - stores monetary amount as float
    # TODO: Consider using DECIMAL type for better precision with currency
    balance = Column(Float)