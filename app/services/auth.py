# app/services/auth.py

from app.schemas.user import UserCreate, UserResponse
from app.utils.security import verify_password, get_password_hash
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.models.user import UserModel
from app.services.user_service import get_user_by_email, create_user_in_db

# Secret key for JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

async def create_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        return None
    user_dict = user.dict()
    user_dict["password_hash"] = get_password_hash(user.password)
    user_dict["user_id"] = user.email  # Or generate a unique ID
    user_dict["online_status"] = False
    user_dict["last_active"] = datetime.utcnow()
    new_user = UserModel(**user_dict)
    await create_user_in_db(new_user)
    return UserResponse(**new_user.dict())

async def authenticate_user(email: str, password: str):
    user = await get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user_by_email(user_id)
    if user is None:
        raise credentials_exception
    return user
