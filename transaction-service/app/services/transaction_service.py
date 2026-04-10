from app.repositories.transaction_repo import TransactionRepository
from app.core.kafka_producer import send_transaction_event
from app.core.logger import get_logger

logger = get_logger(__name__)

class TransactionService:

    def __init__(self):
        self.txn_repo = TransactionRepository()
       

    def transfer(self, db, data):
        try:
            logger.info(f"Transfer started: {data.from_account} → {data.to_account}")

            event = {
                "from_account": data.from_account,
                "to_account" : data.to_account,
                "amount" : data.amount
            }
            send_transaction_event(event)

        except Exception as e:
           
            logger.error(f"Transaction failed: {str(e)}")
            return {"error": str(e)}