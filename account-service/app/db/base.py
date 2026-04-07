"""
Database Base Configuration
Defines the base class for all SQLAlchemy ORM models.
This is the declarative base that all database models inherit from.
"""
from sqlalchemy.orm import declarative_base

# Create the declarative base class
# All database model classes must inherit from this Base class
# This allows SQLAlchemy to track and map Python classes to database tables
Base = declarative_base()