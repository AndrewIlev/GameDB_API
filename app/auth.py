from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    truncated_password = password[:72].encode("utf-8")
    return pwd_context.hash(truncated_password)

def verify_password(plain: str, hashed: str) -> bool:
    truncated_plain = plain[:72].encode("utf-8")
    return pwd_context.verify(truncated_plain, hashed)

def create_access_token(subject: str, expires_delta: timedelta = timedelta(minutes=60)):
    expire = datetime.utcnow() + expires_delta
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token_get_username(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None


