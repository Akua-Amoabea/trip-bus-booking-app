from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.config.config import settings

from passlib.context import CryptContext



pwd_hash =CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_hash.hash(password)


def verify_password(password:str, hashed_password: str):
    return pwd_hash.verify(password, hashed_password)


def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt



def verify_token(token:str):
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=settings.ALGORITHM
        )

        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inavalid Token"
        )

def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(days=30)

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def verify_refresh_token(token:str):
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_KEY,
            algorithms=settings.ALGORITHM
        )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token"
            )

        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        
        )
    

    


    