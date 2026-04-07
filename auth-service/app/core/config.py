"""
Configuration module for Auth Service
Handles all environment variables and security settings.
Manages JWT token configuration and database connections.
"""
import os

class Settings:
    """
    Settings class that loads configuration from environment variables.
    Includes database connection and JWT authentication parameters.
    """
    # Database Configuration
    # Constructs MySQL connection URL from environment or uses default
    # Format: mysql+pymysql://username:password@host:port/database_name
    DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:root@localhost:3306/auth_db")
    
    # JWT (JSON Web Token) Configuration
    # SECRET_KEY: Used to sign and verify JWT tokens
    # ⚠️ WARNING: In production, load from secure environment variable, not hardcoded!
    # Used for: token.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    SECRET_KEY = "mysecretkey"
    
    # JWT Algorithm: Standard algorithm for encoding/decoding tokens
    # HS256 (HMAC-SHA256): Symmetric algorithm, both sign and verify use same secret key
    # Alternative: RS256 (asymmetric) for public-private key pairs
    ALGORITHM = "HS256"

# Global settings instance used throughout the application
# Import this in any module that needs settings: from app.core.config import settings
settings = Settings()