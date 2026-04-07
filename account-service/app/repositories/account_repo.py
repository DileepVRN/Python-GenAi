from sqlalchemy.orm import Session
from app.models.account import Account

class AccountRepository:

    def create(self, db: Session, data):
        account = Account(name=data.name, balance=data.balance)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

    def get_all(self, db: Session):
        return db.query(Account).all()