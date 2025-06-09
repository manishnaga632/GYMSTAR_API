
from sqlalchemy.orm import Session
from api.database.models.membership_plans import MembershipPlan
from api.database.schemas.membership_plans import MembershipPlanCreate, MembershipPlanUpdate

def calculate_final_price(price: float, discount_type: str, discount_value: float) -> float:
    if discount_type == "percent":
        return price - (price * discount_value / 100)
    elif discount_type == "amount":
        return price - discount_value
    return price

def create_plan(db: Session, plan: MembershipPlanCreate):
    final_price = plan.price
    if plan.discount_type and plan.discount_value:
        final_price = calculate_final_price(plan.price, plan.discount_type, plan.discount_value)

    db_plan = MembershipPlan(
        name=plan.name,
        price=plan.price,
        duration=plan.duration,
        status=plan.status,
        discount_type=plan.discount_type,
        discount_value=plan.discount_value,
        final_price=final_price
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def get_plan_by_id(db: Session, plan_id: int):
    return db.query(MembershipPlan).filter(MembershipPlan.id == plan_id).first()

def get_all_plans(db: Session):
    return db.query(MembershipPlan).all()

def update_plan(db: Session, plan_id: int, update_data: MembershipPlanUpdate):
    plan = get_plan_by_id(db, plan_id)
    if not plan:
        return None

    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(plan, field, value)

    # Recalculate final price
    discount_type = update_data.discount_type if update_data.discount_type is not None else plan.discount_type
    discount_value = update_data.discount_value if update_data.discount_value is not None else plan.discount_value
    price = update_data.price if update_data.price is not None else plan.price

    if discount_type and discount_value is not None:
        plan.final_price = calculate_final_price(price, discount_type, discount_value)
    else:
        plan.final_price = price

    db.commit()
    db.refresh(plan)
    return plan

def delete_plan(db: Session, plan_id: int):
    plan = get_plan_by_id(db, plan_id)
    if not plan:
        return None
    db.delete(plan)
    db.commit()
    return plan

