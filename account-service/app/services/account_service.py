"""
Account Service Layer
Business logic for account operations.
Acts as intermediary between API endpoints and repository layer.
"""
from app.repositories.account_repo import AccountRepository

class AccountService:
    """
    Service class for account business logic.
    - Handles account creation and retrieval
    - Coordinates between API endpoints and database repository
    - Can be extended with validation, transactions, and calculations
    """

    def __init__(self):
        """
        Initialize service with repository instance.
        Creates singleton repository for all operations.
        """
        # Initialize repository instance for database operations
        self.repo = AccountRepository()

    def create_account(self, db, data):
        """
        Business logic for creating a new account.
        
        Args:
            db: SQLAlchemy database session
            data: AccountCreate schema with account details
            
        Returns:
            Account: Created account object with ID
            
        TODO: Add validation, business rules, and error handling
        """
        # Delegate database operation to repository
        return self.repo.create(db, data)

    def get_accounts(self, db):
        """
        Business logic for retrieving all accounts.
        
        Args:
            db: SQLAlchemy database session
            
        Returns:
            List[Account]: All accounts in the system
            
        TODO: Add pagination, filtering, and sorting
        """
        # Delegate to repository to fetch all accounts
        return self.repo.get_all(db)