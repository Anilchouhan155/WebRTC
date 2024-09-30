# app/models/user.py

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class UserModel(BaseModel):
    user_id: str
    username: str
    email: str
    password_hash: str
    profile_info: dict
    preferences: dict
    online_status: bool = False
    last_active: datetime = Field(default_factory=datetime.utcnow)
