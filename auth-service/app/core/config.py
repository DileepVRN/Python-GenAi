import os

class Settings:
    DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:root@localhost:3306/auth_db")
    SECRET_KEY = "mysecretkey"
    ALGORITHM = "HS256"

settings = Settings()