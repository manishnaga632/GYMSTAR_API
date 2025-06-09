from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.subscription import SubscriptionCreate, SubscriptionUpdate, SubscriptionResponse
from api.crud import subscription as crud_sub
from api.token import get_current_user
from api.database.models.user import User

router = APIRouter()

@router.post("/create", response_model=SubscriptionResponse)
def create_subscription(sub: SubscriptionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return crud_sub.create_subscription(db, sub, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_all", response_model=list[SubscriptionResponse])
def get_all_subscriptions(db: Session = Depends(get_db)):
    return crud_sub.get_all_subscriptions(db)

@router.get("/user_subscription", response_model=list[SubscriptionResponse])
def get_user_subscriptions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud_sub.get_subscriptions_by_user(db, current_user.id)

@router.put("/update/{subscription_id}", response_model=SubscriptionResponse)
def update_subscription(subscription_id: int, sub_update: SubscriptionUpdate, db: Session = Depends(get_db)):
    try:
        return crud_sub.update_subscription(db, subscription_id, sub_update)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{subscription_id}")
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    try:
        return crud_sub.delete_subscription(db, subscription_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))