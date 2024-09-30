# app/routers/auth.py

from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.auth import authenticate_user, create_access_token, create_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    new_user = await create_user(user)
    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )
    return new_user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials"
        )
    access_token = create_access_token(data={"sub": user.user_id})
    return {"access_token": access_token, "token_type": "bearer"}
