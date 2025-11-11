# routes/auth.py

import os
from datetime import UTC, datetime, timedelta
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
import jwt
from sqlmodel import Session, select
from db import get_session

from models.user import User

router = APIRouter()
load_dotenv()


APP_SECRET = os.getenv("JWT_SECRET")
TOKEN_TIME_LIMIT = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=TOKEN_TIME_LIMIT)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, APP_SECRET, algorithm=ALGORITHM)
    return encoded_jwt

# creating a funciton that will decode the jwt, validate it and return the User
def jwt_verification_function(
        token: str = Depends(oauth2_schema),
        db: Session = Depends(get_session)
)-> User:
    
    credentails_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="couldnt validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    
    try:
        payload = jwt.decode(token, APP_SECRET, algorithms=[ALGORITHM])

        email: str = payload.get("sub")
        if email is None:
            raise credentails_exception
        
        # verifying the user in db

        query = select(User).where(User.email==email)
        user = db.exec(query).first()

        if user is None:
            raise credentails_exception

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Token has expired",
            headers={"WWW-Authenticate":"Bearer"}
        )
    
    except jwt.InvalidTokenError:
        raise credentails_exception





@router.post("/login")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session)
):
   
    # only verifying email since its a hackathon
    query = select(User).where(User.email == form_data.username)
    user = db.exec(query).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password", 
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create the token with user's email and role
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}
    )
    
    return {"access_token": access_token, "token_type": "bearer", "role": user.role}