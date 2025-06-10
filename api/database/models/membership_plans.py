from sqlalchemy import Column, Integer, String, Float, Enum as SqlEnum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from api.database.connection import Base
import enum

class DurationEnum(str, enum.Enum):
    Monthly = "Monthly"
    Half_Yearly = "Half_Yearly"
    Yearly = "Yearly"

class StatusEnum(str, enum.Enum):
    Yes = "Yes"
    No = "No"

class DiscountTypeEnum(str, enum.Enum):
    percent = "percent"
    amount = "amount"

class MembershipPlan(Base):
    __tablename__ = "membership_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    duration = Column(SqlEnum(DurationEnum), nullable=False)
    status = Column(SqlEnum(StatusEnum), default=StatusEnum.Yes, nullable=False)

    discount_type = Column(SqlEnum(DiscountTypeEnum), nullable=True)
    discount_value = Column(Float, nullable=True)
    final_price = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)



    subscriptions = relationship("Subscription", back_populates="membership_plan")
