from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

from .ca_config import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRES_IN
from .UserInfo import UserInfoProcessor

class JWTProcessor:

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    user_info = UserInfoProcessor()

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def login_for_access_token(self, username, password):
        user = self.user_info.user_login(username=username, password=password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="Incorrect username or password",
                                headers={"WWW-Authenticate": "Bearer"})
        access_token_expires = timedelta(hours=ACCESS_TOKEN_EXPIRES_IN)
        access_token = self.create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
        return {
            "username": user["username"],
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": str(access_token_expires)
        }
    
    def validate_jwt_token(self, token):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            print("username on validate is: ", username)
            return True
        except JWTError:
            return False