from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base   # IMPORTANT

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    balance = Column(Float)