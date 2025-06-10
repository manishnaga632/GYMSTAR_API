from pydantic import BaseModel, Field, model_validator, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime


class DurationEnum(str, Enum):
    Monthly = "Monthly"
    Half_Yearly = "Half_Yearly"
    Yearly = "Yearly"


class StatusEnum(str, Enum):
    Yes = "Yes"
    No = "No"


class DiscountTypeEnum(str, Enum):
    percent = "percent"
    amount = "amount"


class MembershipPlanBase(BaseModel):
    name: str
    price: float
    duration: DurationEnum
    status: StatusEnum = StatusEnum.Yes
    discount_type: Optional[DiscountTypeEnum] = None
    discount_value: Optional[float] = None

    @model_validator(mode="after")
    def validate_discount(self):
        dtype = self.discount_type
        dval = self.discount_value
        price = self.price

        if dtype is not None and dval is None:
            raise ValueError("Discount value must be provided with discount type")

        if dtype == "percent":
            if dval is not None and (dval < 0 or dval > 100):
                raise ValueError("Percent discount must be between 0 and 100")
        elif dtype == "amount":
            if dval is not None:
                if dval <= 0:
                    raise ValueError("Amount discount must be greater than 0")
                if dval > price:
                    raise ValueError("Amount discount cannot be greater than the original price")
        return self


class MembershipPlanCreate(MembershipPlanBase):
    pass


class MembershipPlanUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    duration: Optional[DurationEnum] = None
    status: Optional[StatusEnum] = None
    discount_type: Optional[DiscountTypeEnum] = None
    discount_value: Optional[float] = None

    @model_validator(mode="after")
    def validate_discount(self):
        dtype = self.discount_type
        dval = self.discount_value
        price = self.price

        if dtype is not None and dval is None:
            raise ValueError("Discount value must be provided with discount type")

        if dtype == "percent":
            if dval is not None and (dval < 0 or dval > 100):
                raise ValueError("Percent discount must be between 0 and 100")
        elif dtype == "amount":
            if dval is not None:
                if dval <= 0:
                    raise ValueError("Amount discount must be greater than 0")
                if price is not None and dval > price:
                    raise ValueError("Amount discount cannot be greater than the original price")
        return self


class MembershipPlanResponse(MembershipPlanBase):
    id: int
    price: Optional[float] = None
    discount_value: Optional[float] = None
    final_price: Optional[float]
    duration: Optional[DurationEnum] = None

    model_config = ConfigDict(from_attributes=True)
