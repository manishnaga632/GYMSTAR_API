from sqlalchemy import Column, Integer, String
from api.database.base import Base

class AdminProfile(Base):
    __tablename__ = "admin_profiles"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255), index=True)  
    mobile_number = Column(String(15))  
    email = Column(String(255), unique=True, index=True, nullable=False)

    twitter_link = Column(String(255), nullable=True)
    linkedin_link = Column(String(255), nullable=True)
    facebook_link = Column(String(255), nullable=True)
    insta_link = Column(String(255), nullable=True)
    youtube_link = Column(String(255), nullable=True)
    experience_in_year = Column(Integer)
    total_trainers = Column(Integer)
    complete_project_number = Column(Integer)
    happy_clients_number = Column(Integer)
    

