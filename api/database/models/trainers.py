from sqlalchemy import Column, Integer, String
from api.database.base import Base

class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    mobile_number = Column(String(20), nullable=False)
    twitter_link = Column(String(255), nullable=True)
    facebook_link = Column(String(255), nullable=True)
    linkdin_link = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
