from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional

class AdminProfileBase(BaseModel):
    address: str
    mobile_number: str
    email:EmailStr
    twitter_link: Optional[str] = None
    linkedin_link: Optional[str] = None
    facebook_link: Optional[str] = None
    insta_link: Optional[str] = None
    youtube_link: Optional[str] = None
    experience_in_year: int
    total_trainers: int
    complete_project_number: int
    happy_clients_number: int

class AdminProfileCreate(AdminProfileBase):
    pass

class AdminProfileUpdate(AdminProfileBase):
    pass

class AdminProfileOut(AdminProfileBase):
    id: int


    model_config = ConfigDict(from_attributes=True)


