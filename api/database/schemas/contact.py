from pydantic import BaseModel, EmailStr
from datetime import datetime

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class ContactResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    subject: str
    message: str
    seen: bool  

    created_at: datetime

    class Config:
        from_attributes = True
