# from sqlalchemy import Column, Integer, String
# from api.database.base import Base  # Adjust this import as per your structure

# class Contact(Base):
#     __tablename__ = "contacts"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(100), nullable=False)
#     subject = Column(String(200), nullable=False)
#     message = Column(String(1000), nullable=False)
from sqlalchemy import Column, Integer, String, Text, DateTime,Boolean
from datetime import datetime
from api.database.connection import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    subject = Column(String(200))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    seen = Column(Boolean, default=False)  

