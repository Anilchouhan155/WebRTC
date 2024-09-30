# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserResponse, UserUpdate
from app.services.auth import get_current_user
from app.services.user_service import get_user_by_id, update_user

router = APIRouter()

@router.get("/user/me", response_model=UserResponse)
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user

@router.put("/user/me", response_model=UserResponse)
async def update_user_profile(user_update: UserUpdate, current_user=Depends(get_current_user)):
    updated_user = await update_user(current_user.user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user
