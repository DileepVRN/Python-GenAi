from app.models.transaction import Transaction

class TransactionRepository:

    def save(self, db, txn_data):
        txn = Transaction(
            from_account=txn_data.from_account,
            to_account=txn_data.to_account,
            amount=txn_data.amount
        )
        db.add(txn)
        return txn