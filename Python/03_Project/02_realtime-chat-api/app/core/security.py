#contain the authentication and security logic

# 1. Hash Passwords
#           ↓
# 2. Verify Passwords
#           ↓
# 3. Create JWT Tokens
#           ↓
# 4. Decode JWT Tokens


from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings

password_context = CryptContext(
    schemas=["bcrypt"],
    deprecated="auto"
)



def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password:str, hashed_password: str) -> str:
    return password_context.verify(plain_password, hashed_password)


def create_access_token(data: dict)-> str:
    to_encode = data.copy()


    expire= datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


def decode_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None