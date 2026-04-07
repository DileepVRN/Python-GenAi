"""
Database Base Configuration
Defines the base class for all SQLAlchemy ORM models.
All database model classes in auth-service inherit from this Base.
"""
from sqlalchemy.orm import declarative_base

# Create the declarative base class
# All database model classes must inherit from this Base class
# This allows SQLAlchemy to track and map Python classes to database tables
# Example: class User(Base): automatically becomes a mapped ORM model
Base = declarative_base()