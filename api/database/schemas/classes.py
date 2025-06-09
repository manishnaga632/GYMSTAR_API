from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ✅ Common Schema
class ClassBase(BaseModel):
    trainer_id: int
    day: str
    class_name: str
    timeing: str

# ✅ Create Schema
class ClassCreate(ClassBase):
    pass

# ✅ Response Schema
class ClassOut(ClassBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
