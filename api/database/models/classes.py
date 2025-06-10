from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from api.database.base import Base

class ClassModel(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))
    day = Column(String(20), nullable=False)         # e.g. 'Monday'
    class_name = Column(String(100), nullable=False) # e.g. 'Yoga Basics'
    timeing = Column(String(50), nullable=False)     # e.g. '7:00 AM - 8:00 AM'
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
