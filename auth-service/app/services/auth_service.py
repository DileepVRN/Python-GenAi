"""
Auth Service Layer
Business logic for authentication operations.
Handles user registration, login, password hashing, and JWT token generation.
Acts as intermediary between API endpoints and repository layer.
"""
from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_token

class AuthService:
    """
    Service class for authentication business logic.
    - Handles user registration with password hashing
    - Handles user login with credential verification
    - Generates JWT tokens for authenticated users
    - Coordinates between API endpoints and database repository
    """

    def __init__(self):
        """
        Initialize service with repository instance.
        Creates singleton repository for user database operations.
        """
        # Initialize repository instance for database operations
        self.repo = UserRepository()

    def register(self, db, data):
        """
        Business logic for user registration.
        1. Validates input data
        2. Hashes password using bcrypt
        3. Creates user in database
        
        Args:
            db: SQLAlchemy database session
            data: UserCreate schema with username and password
            
        Returns:
            User: Created user object, or error dict if validation fails
            
        Error Cases:
            - Missing password: Returns {"error": "Password is required"}
            - Duplicate username: Database will raise IntegrityError (TODO: handle)
        """
        # DEBUG: Print incoming registration data (remove in production)
        print("Incoming:", data.username, data.password)

        # Validation: Check if password is provided
        if not data.password:
            return {"error": "Password is required"}

        # Hash the plain text password using bcrypt
        # IMPORTANT: Never store plain text passwords!
        # hash_password() handles passwords > 72 bytes via SHA256
        hashed = hash_password(data.password)
        
        # Delegate to repository to create user with hashed password
        return self.repo.create(db, data.username, hashed)

    def login(self, db, data):
        """
        Business logic for user login.
        1. Finds user by username
        2. Verifies password matches stored hash
        3. Generates JWT token if credentials valid
        
        Args:
            db: SQLAlchemy database session
            data: UserLogin schema with username and password
            
        Returns:
            dict: {"access_token": token_string} on success
            dict: {"error": "Invalid credentials"} on failure
            
        Error Cases:
            - User not found
            - Password doesn't match stored hash
        """
        # Lookup user by username in database
        user = self.repo.get_by_username(db, data.username)

        # Validation: Check if user exists AND password matches
        # verify_password() compares plain text with bcrypt hash
        if not user or not verify_password(data.password, user.password):
            # Generic error message prevents username enumeration
            return {"error": "Invalid credentials"}

        # Generate JWT token for authenticated user
        # Token contains username ("sub" claim) and expiration time
        # Token expires in 1 hour (see create_token in security.py)
        token = create_token({"sub": user.username})
        
        # Return token to client for authenticated requests
        return {"access_token": token}