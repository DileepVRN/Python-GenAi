"""
Database Session Configuration
Manages SQLAlchemy database connections and sessions for auth-service.
Provides session factory for creating database transactions.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create SQLAlchemy engine
# Engine manages database connections and connection pooling
# Uses MySQL connection string from settings
engine = create_engine(settings.DB_URL)

# Create session factory
# SessionLocal() creates a new database session for each use
# bind=engine: Associates this session maker with our database engine
# Sessions manage transactions and ORM object lifecycle
SessionLocal = sessionmaker(bind=engine)