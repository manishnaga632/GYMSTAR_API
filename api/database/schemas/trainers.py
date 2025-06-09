from pydantic import BaseModel
from typing import Optional

class TrainerBase(BaseModel):
    name: str
    designation: str
    mobile_number: str
    twitter_link: Optional[str]
    facebook_link: Optional[str]
    linkdin_link: Optional[str]
    image: Optional[str]

class TrainerCreate(TrainerBase):
    pass

class TrainerUpdate(TrainerBase):
    pass

class TrainerOut(TrainerBase):
    id: int

    class Config:
        from_attributes = True
