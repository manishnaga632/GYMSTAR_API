from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from api.database.base import Base

class Slider(Base):
    __tablename__ = "sliders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    sub_title = Column(String(255), nullable=True)
    image = Column(String(255), nullable=False)
    status = Column(String(10), default="no")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
