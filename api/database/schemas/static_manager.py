from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StaticBase(BaseModel):
    tital: str
    containt: str

class StaticCreate(StaticBase):
    pass

class StaticUpdate(StaticBase):
    pass

class StaticOut(StaticBase):
    id: int
    created_at: Optional[datetime]
    update_at: Optional[datetime]

    class Config:
        from_attributes = True
