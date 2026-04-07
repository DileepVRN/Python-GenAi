"""
Account Repository Layer
Handles all database operations for Account model.
Implements the repository pattern to abstract database access.
"""
from sqlalchemy.orm import Session
from app.models.account import Account

class AccountRepository:
    """
    Repository class for Account entity.
    Encapsulates all database queries and operations.
    Provides clean interface between service layer and database.
    """

    def create(self, db: Session, data):
        """
        Creates a new account in the database.
        
        Args:
            db (Session): SQLAlchemy database session
            data: AccountCreate schema with name and balance
            
        Returns:
            Account: The created account object with generated ID
        """
        # Create new Account ORM model instance from Pydantic schema
        account = Account(name=data.name, balance=data.balance)
        
        # Add account to session (staged for insert)
        db.add(account)
        
        # Commit transaction - writes to database
        db.commit()
        
        # Refresh from database to get auto-generated ID
        db.refresh(account)
        
        return account

    def get_all(self, db: Session):
        """
        Retrieves all accounts from the database.
        
        Args:
            db (Session): SQLAlchemy database session
            
        Returns:
            List[Account]: List of all account objects
        """
        # Query all accounts from the accounts table
        return db.query(Account).all()