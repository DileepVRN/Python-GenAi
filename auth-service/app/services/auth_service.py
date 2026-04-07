from app.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_token

class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    def register(self, db, data):
        print("Incoming:", data.username, data.password)  # DEBUG

        if not data.password:
            return {"error": "Password is required"}

        hashed = hash_password(data.password)
        return self.repo.create(db, data.username, hashed)

    def login(self, db, data):
        user = self.repo.get_by_username(db, data.username)

        if not user or not verify_password(data.password, user.password):
            return {"error": "Invalid credentials"}

        token = create_token({"sub": user.username})
        return {"access_token": token}