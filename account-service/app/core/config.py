import os

class Settings:
    PROJECT_NAME = "Account Service"
    DB_URL = os.getenv("DB_URL", "mysql+pymysql://root:root@localhost:3306/account_db")

settings = Settings()