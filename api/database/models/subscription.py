from sqlalchemy import Column, Integer, Float, Date, ForeignKey, Enum as SqlEnum, Boolean
from sqlalchemy.orm import relationship
from api.database.connection import Base
import enum

class PaymentStatusEnum(str, enum.Enum):
    paid = "paid"
    failed = "failed"
    pending = "pending"

class DurationEnum(str, enum.Enum):
    Monthly = "Monthly"
    Half_Yearly = "Half_Yearly"
    Yearly = "Yearly"

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    membership_plan_id = Column(Integer, ForeignKey("membership_plans.id"), nullable=False)

    duration = Column(SqlEnum(DurationEnum), nullable=True)
    start_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)

    final_price = Column(Float, nullable=False)
    payment_status = Column(SqlEnum(PaymentStatusEnum), default=PaymentStatusEnum.pending, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)

    user = relationship("User", back_populates="subscriptions")
    membership_plan = relationship("MembershipPlan", back_populates="subscriptions")

