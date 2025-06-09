from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum

class PaymentStatusEnum(str, Enum):
    paid = "paid"
    failed = "failed"
    pending = "pending"

class DurationEnum(str, Enum):
    Monthly = "Monthly"
    Half_Yearly = "Half_Yearly"
    Yearly = "Yearly"

class SubscriptionBase(BaseModel):
    membership_plan_id: int
    payment_status: Optional[PaymentStatusEnum] = PaymentStatusEnum.pending

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionUpdate(BaseModel):
    payment_status: Optional[PaymentStatusEnum] = None
    is_active: Optional[bool] = None

class SubscriptionResponse(SubscriptionBase):
    id: int
    user_id: int
    start_date: Optional[date]
    expiry_date: Optional[date]
    final_price: float
    is_active: bool
    duration: Optional[DurationEnum]

    class Config:
        from_attributes = True