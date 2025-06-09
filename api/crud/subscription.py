from sqlalchemy.orm import Session
from datetime import date
from api.database.models.subscription import Subscription, PaymentStatusEnum
from api.database.models.membership_plans import MembershipPlan
from api.database.schemas.subscription import SubscriptionCreate, SubscriptionUpdate
from dateutil.relativedelta import relativedelta


def calculate_expiry(start_date: date, duration: str) -> date:
    if duration == "Monthly":
        return start_date + relativedelta(months=1)
    elif duration == "Half_Yearly":
        return start_date + relativedelta(months=6)
    elif duration == "Yearly":
        return start_date + relativedelta(years=1)
    else:
        raise ValueError("Invalid duration")


def create_subscription(db: Session, sub: SubscriptionCreate, user_id: int):
    plan = db.query(MembershipPlan).filter(
        MembershipPlan.id == sub.membership_plan_id,
        MembershipPlan.status == "Yes"
    ).first()
    
    if not plan:
        raise Exception("Membership plan not found or not active")

    # ✅ Check for an active existing subscription
    existing_sub = db.query(Subscription).filter(
        Subscription.user_id == user_id,
        Subscription.is_active == True
    ).first()

    if existing_sub:
        # Compare final_price to allow only if new plan is an upgrade
        if plan.final_price <= existing_sub.final_price:
            raise Exception("You already have an active plan. You can only upgrade to a higher plan.")

    # ✅ Determine start_date, expiry_date, and is_active based on payment status
    start_date = None
    expiry_date = None
    is_active = False

    if sub.payment_status == PaymentStatusEnum.paid:
        start_date = date.today()
        expiry_date = calculate_expiry(start_date, plan.duration)
        is_active = True

    new_sub = Subscription(
        user_id=user_id,
        membership_plan_id=sub.membership_plan_id,
        duration=plan.duration,
        start_date=start_date,
        expiry_date=expiry_date,
        final_price=plan.final_price,
        payment_status=sub.payment_status,
        is_active=is_active
    )

    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub


def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()


def get_subscriptions_by_user(db: Session, user_id: int):
    return db.query(Subscription).filter(Subscription.user_id == user_id).all()



def update_subscription(db: Session, subscription_id: int, sub_update: SubscriptionUpdate):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not subscription:
        raise Exception("Subscription not found")

    if subscription.payment_status == PaymentStatusEnum.Paid:
        if sub_update.payment_status and sub_update.payment_status != PaymentStatusEnum.paid:
            raise Exception("Cannot change payment status of a Paid subscription")

        if sub_update.is_active is not None and sub_update.is_active != True:
            raise Exception("Cannot deactivate a Paid subscription")
    else:
        if sub_update.payment_status:
            subscription.payment_status = sub_update.payment_status

            if sub_update.payment_status == PaymentStatusEnum.paid:
                subscription.start_date = date.today()
                subscription.expiry_date = calculate_expiry(subscription.start_date, subscription.duration)
                subscription.is_active = True
            else:
                subscription.start_date = None
                subscription.expiry_date = None
                subscription.is_active = False

        if sub_update.is_active is not None:
            subscription.is_active = sub_update.is_active

    db.commit()
    db.refresh(subscription)
    return subscription


def delete_subscription(db: Session, subscription_id: int):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if not subscription:
        raise Exception("Subscription not found")
    db.delete(subscription)
    db.commit()
    return {"detail": "Subscription deleted successfully"}