"""
Database Session Configuration
Manages SQLAlchemy database connections and sessions.
Provides session factory for creating database transactions.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create SQLAlchemy engine
# - pool_pre_ping=True: Verifies connection is alive before using it from the pool
#   This prevents "lost connection" errors in long-running applications
engine = create_engine(settings.DB_URL, pool_pre_ping=True)

# Create session factory
# - autocommit=False: Requires explicit commit() for transaction persistence
# - autoflush=False: Requires explicit flush() before queries (better control)
# - bind=engine: Binds this session factory to our database engine
# Use this factory to get a new database session for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)