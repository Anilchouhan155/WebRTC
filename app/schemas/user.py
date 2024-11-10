# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    user_id: str
    naem: str
    profile_info: Optional[dict]
    preferences: Optional[dict]
    online_status: bool
    last_active: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    profile_info: Optional[dict]
    preferences: Optional[dict]

class Token(BaseModel):
    access_token: str
    token_type: str
