from app.repositories.account_repo import AccountRepository

class AccountService:

    def __init__(self):
        self.repo = AccountRepository()

    def create_account(self, db, data):
        return self.repo.create(db, data)

    def get_accounts(self, db):
        return self.repo.get_all(db)