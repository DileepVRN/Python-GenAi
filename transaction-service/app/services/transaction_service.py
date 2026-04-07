from app.repositories.transaction_repo import TransactionRepository
from app.repositories.account_repo import AccountRepository
from app.core.logger import get_logger

logger = get_logger(__name__)

class TransactionService:

    def __init__(self):
        self.txn_repo = TransactionRepository()
        self.acc_repo = AccountRepository()

    def transfer(self, db, data):
        try:
            logger.info(f"Transfer started: {data.from_account} → {data.to_account}")

            sender = self.acc_repo.get_by_id(db, data.from_account)
            receiver = self.acc_repo.get_by_id(db, data.to_account)

            if not sender or not receiver:
                logger.error("Account not found")
                return {"error": "Account not found"}

            if sender.balance < data.amount:
                logger.warning("Insufficient balance")
                return {"error": "Insufficient balance"}

            sender.balance -= data.amount
            receiver.balance += data.amount

            self.txn_repo.save(db, data)

            db.commit()

            logger.info("Transaction successful")

            return {"message": "Transfer successful"}

        except Exception as e:
            db.rollback()
            logger.error(f"Transaction failed: {str(e)}")
            return {"error": str(e)}