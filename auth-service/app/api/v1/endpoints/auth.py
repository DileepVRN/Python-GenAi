"""
Auth API Endpoints (v1)
Declares HTTP routes for authentication operations.
Handles user registration, login, and JWT token generation.
Manages request/response validation and database session injection.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.auth_service import AuthService
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserLogin

# ========== ROUTER SETUP ==========
# Create APIRouter instance to group related endpoints
# Router will be included in main.py with prefix "/auth"
router = APIRouter()

# ========== SERVICE INSTANCE ==========
# Create single service instance for all endpoint handlers
# Handles authentication business logic and service coordination
service = AuthService()

# ========== DATABASE DEPENDENCY ==========
def get_db():
    """
    Dependency injection for database sessions.
    FastAPI automatically calls this for routes with db parameter.
    
    Ensures:
    1. Fresh database session created for each request
    2. Session is properly closed after request completes
    3. Transactions are isolated per request
    
    Yields:
        Session: SQLAlchemy database session for the request
    """
    # Create new database session from session factory
    db = SessionLocal()
    try:
        # Yield session to route handler
        yield db
    finally:
        # Always close session after request completes
        # Prevents database connection leaks
        db.close()

# ========== ENDPOINTS ==========

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    User Registration Endpoint
    Creates a new user account with hashed password.
    
    HTTP METHOD: POST
    ENDPOINT: POST /auth/register
    
    Request body (JSON):
        {
            "username": "john_doe",
            "password": "SecurePassword123"
        }
    
    Response (Success - 200):
        {
            "id": 1,
            "username": "john_doe",
            "password": "$2b$12$...(bcrypt_hash)..."
        }
    
    Response (Error - 400):
        {
            "error": "Password is required"
        }
    
    Error Cases:
        - Missing username: Pydantic validation error
        - Missing password: Validation by auth_service.register()
        - Duplicate username: Database IntegrityError (TODO: handle gracefully)
    
    Args:
        user (UserCreate): Validated request data with username and password
        db (Session): Injected database session dependency
        
    Returns:
        dict: Created user object or error message
        
    Security Notes:
        - Password is hashed using bcrypt before storage
        - Plain text password never stored in database
        - Passwords over 72 bytes are SHA256-hashed first (bcrypt limitation)
    """
    # Call service to register user (validation + hashing + persistence)
    return service.register(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    User Login Endpoint
    Authenticates user with username and password.
    Returns JWT token for authenticated requests.
    
    HTTP METHOD: POST
    ENDPOINT: POST /auth/login
    
    Request body (JSON):
        {
            "username": "john_doe",
            "password": "SecurePassword123"
        }
    
    Response (Success - 200):
        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "token_type": "bearer"
        }
    
    Response (Error - 401):
        {
            "error": "Invalid credentials"
        }
    
    Error Cases:
        - User not found: Returns generic error (prevents username enumeration)
        - Password mismatch: Returns generic error
        - Missing fields: Pydantic validation error
    
    Args:
        user (UserLogin): Validated request data with username and password
        db (Session): Injected database session dependency
        
    Returns:
        dict: JWT access token if credentials valid, error message if invalid
        
    Token Format:
        - Type: JWT (JSON Web Token)
        - Algorithm: HS256 (HMAC-SHA256)
        - Payload: {"sub": username, "exp": expiration_timestamp}
        - Expiration: 1 hour from generation
        - Usage: Include in Authorization header as "Bearer <token>"
        
    Security Notes:
        - Password verified against bcrypt hash (never plain text comparison)
        - Generic error message prevents username enumeration attacks
        - Token expires after 1 hour (see core/security.py)
    """
    # Call service to authenticate user and generate token
    return service.login(db, user)