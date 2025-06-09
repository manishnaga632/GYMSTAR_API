from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from api.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    mobile = Column(String(15), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False, default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    subscriptions = relationship("Subscription", back_populates="user")
