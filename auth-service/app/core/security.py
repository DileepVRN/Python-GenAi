from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings
from app.core.logger import get_logger
import hashlib
logger = get_logger(__name__)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔥 Fix for long passwords
def hash_password(password: str):
    # Convert long password to fixed length using SHA256
    password_bytes = password.encode("utf-8")
    logger.info(f"inside hasing logic{password} ")
    if len(password_bytes) > 72:
        password = hashlib.sha256(password_bytes).hexdigest()
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain_bytes = plain.encode("utf-8")

    if len(plain_bytes) > 72:
        plain = hashlib.sha256(plain_bytes).hexdigest()
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)