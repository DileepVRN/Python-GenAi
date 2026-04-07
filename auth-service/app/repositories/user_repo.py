from app.models.user import User

class UserRepository:

    def get_by_username(self, db, username):
        return db.query(User).filter(User.username == username).first()

    def create(self, db, username, password):
        user = User(username=username, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user