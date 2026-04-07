"""
User Repository Layer
Handles all database operations for User model.
Implements the repository pattern to abstract database access.
Provides clean interface for user queries and creation.
"""
from app.models.user import User

class UserRepository:
    """
    Repository class for User entity.
    Encapsulates all database queries for user operations.
    Methods:
    - get_by_username(): Find user by unique username
    - create(): Create new user account with hashed password
    """

    def get_by_username(self, db, username):
        """
        Retrieves a user from database by username.
        Used during login to fetch credentials for verification.
        
        Args:
            db: SQLAlchemy database session
            username: Unique username to search for
            
        Returns:
            User: User object if found, None if not found
            
        Note: This query uses indexed 'username' column for fast lookup
        """
        # Query users table, filter by username, get first result
        # .first() returns single result or None if no match
        return db.query(User).filter(User.username == username).first()

    def create(self, db, username, password):
        """
        Creates a new user account in the database.
        Called after password hashing during registration.
        
        Args:
            db: SQLAlchemy database session
            username: Unique username for the new account
            password: HASHED password (must be pre-hashed by service layer)
            
        Returns:
            User: Created user object with database ID
            
        IMPORTANT: Password MUST be hashed before calling this method!
        This method assumes password is already bcrypt-hashed.
        """
        # Create new User ORM model instance
        user = User(username=username, password=password)
        
        # Add user to session (staged for insert)
        db.add(user)
        
        # Commit transaction - writes user to database
        # If username is duplicate, this will fail (unique constraint)
        db.commit()
        
        # Refresh from database to get auto-generated ID
        db.refresh(user)
        
        return user