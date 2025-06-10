from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from api.database.base import Base

class StaticManager(Base):
    __tablename__ = "static_manager"

    id = Column(Integer, primary_key=True, index=True)
    tital = Column(String(200), nullable=False)
    containt = Column(String(5000), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
