"""
Configuration module for Account Service
Handles all environment variables and application settings
"""
import os

class Settings:
    """
    Settings class that loads configuration from environment variables.
    Uses MySQL database for account data storage.
    """
    # Project metadata
    PROJECT_NAME = "Account Service"
    
    # Database Configuration
    # Constructs MySQL connection URL from environment or uses default
    # Format: mysql+pymysql://username:password@host:port/database_name
    # pool_pre_ping helps maintain connection health by pinging DB before use
    DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:root@mysql:3306/account_db")

# Global settings instance used throughout the application
settings = Settings()