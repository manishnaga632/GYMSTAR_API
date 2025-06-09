from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SliderBase(BaseModel):
    title: str
    sub_title: Optional[str]
    image: str
    status: Optional[str] = "no"

class SliderCreate(SliderBase):
    pass

class SliderUpdate(SliderBase):
    pass

class SliderOut(SliderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
