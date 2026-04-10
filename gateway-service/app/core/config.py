class Settings:
    AUTH_SERVICE = "http://auth-service:8001"          # internal container port
    ACCOUNT_SERVICE = "http://account-service:8002"
    TRANSACTION_SERVICE = "http://transaction-service:8003"

settings = Settings()