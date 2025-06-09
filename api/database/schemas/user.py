from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    mobile: str
    age: int
    gender: str
    role: Optional[str] = "user"  


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    mobile: str
    age: int
    gender: str
    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdateProfile(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    mobile: Optional[str]
    new_password: Optional[str]
    confirm_password: Optional[str]

class AdminUpdateUser(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    email: Optional[EmailStr]=None
    password: Optional[str]=None
    mobile: Optional[str]=None
    age: Optional[int]=None
    gender: Optional[str]=None
    role: Optional[str]=None

    class Config:
        from_attributes = True




        