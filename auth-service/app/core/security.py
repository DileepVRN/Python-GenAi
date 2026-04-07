"""
Security Module for Auth Service
Handles password hashing, verification, and JWT token generation.
Implements cryptographic security for authentication.
"""
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings
from app.core.logger import get_logger
import hashlib

# Logger instance for security operations
logger = get_logger(__name__)

# ========== PASSWORD HASHING CONFIGURATION ==========
# Create password context using bcrypt algorithm
# schemes=["bcrypt"]: Use bcrypt as the primary hashing algorithm
# deprecated="auto": Automatically handle deprecated algorithms if encountered
# Bcrypt features:
#   - Automatically generates random salt
#   - Configurable work factor (cost) for computational difficulty
#   - One-way hash (cannot reverse to get original password)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ========== PASSWORD HASHING FUNCTIONS ==========

def hash_password(password: str):
    """
    Hash a plain text password using bcrypt.
    
    IMPORTANT FIX for bcrypt limitation:
    - Bcrypt has 72-byte password limit
    - Passwords longer than 72 bytes are hashed with SHA256 first
    - This prevents silent truncation of long passwords
    
    Args:
        password (str): Plain text password to hash
        
    Returns:
        str: Bcrypt hash string (starts with $2b$12$...)
        
    Security Notes:
        - Hash is deterministic given same password (salt generates same hash)
        - Always use verify_password() to compare against stored hash
        - Never store plain text passwords
    """
    # Convert password to bytes
    password_bytes = password.encode("utf-8")
    
    # Log hashing operation (remove sensitive data in production)
    logger.info(f"inside hasing logic{password} ")
    
    # Handle long passwords (> 72 bytes)
    # SHA256 reduces any size password to 64-byte hash
    # Then bcrypt hashes the SHA256 output
    if len(password_bytes) > 72:
        # SHA256 hash as hex string
        password = hashlib.sha256(password_bytes).hexdigest()
    
    # Hash using bcrypt context (adds salt + multiple rounds)
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    """
    Verify a plain text password against a bcrypt hash.
    
    Args:
        plain (str): Plain text password to verify
        hashed (str): Bcrypt hash to verify against (from database)
        
    Returns:
        bool: True if password matches hash, False otherwise
        
    Note: This function handles the same 72-byte limitation as hash_password()
    If password is > 72 bytes, it's SHA256-hashed before bcrypt comparison.
    """
    # Convert password to bytes
    plain_bytes = plain.encode("utf-8")

    # Apply same transformation as hash_password for consistency
    if len(plain_bytes) > 72:
        # SHA256 hash as hex string (same as hash_password)
        plain = hashlib.sha256(plain_bytes).hexdigest()
    
    # Compare plain (possibly hashed) password with stored bcrypt hash
    # pwd_context.verify() extracts salt from stored hash and compares
    return pwd_context.verify(plain, hashed)

# ========== JWT TOKEN FUNCTIONS ==========

def create_token(data: dict):
    """
    Create a signed JWT token for authenticated users.
    
    Token Structure:
        Header: {"alg": "HS256", "typ": "JWT"}
        Payload: data + expiration
        Signature: HMAC-SHA256 signed with SECRET_KEY
    
    Args:
        data (dict): Claims to include in token payload
                    Typically: {"sub": username}
                    
    Returns:
        str: Encoded JWT token as string
        
    Example:
        token = create_token({"sub": "john_doe"})
        # Returns: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        
    JWT Claims Added:
        - exp: Expiration time (UTC timestamp) - 1 hour from now
        - All fields from input data dict
        
    Security Notes:
        - Signed with SECRET_KEY (must be kept secret)
        - Can be verified without database lookup
        - Expiration prevents indefinite token validity
        - Use RS256 in production instead of HS256 (asymmetric)
    """
    # Create copy of input data to avoid modifying original
    to_encode = data.copy()
    
    # Set token expiration to 1 hour from now
    expire = datetime.utcnow() + timedelta(hours=1)
    
    # Add expiration claim to token payload
    to_encode.update({"exp": expire})
    
    # Encode and sign the token using HS256 algorithm
    # - settings.SECRET_KEY: Secret used for HMAC signature
    # - settings.ALGORITHM: "HS256" for HMAC-SHA256
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)