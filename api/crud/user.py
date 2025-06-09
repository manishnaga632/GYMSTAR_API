# ✅ user_crud.py
from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate, UserUpdateProfile, AdminUpdateUser
from api.security import hash_password, verify_password
from fastapi import HTTPException, status
from datetime import datetime


def create_user(db: Session, user: UserCreate):
    # Check for existing email
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check for existing mobile
    if db.query(User).filter(User.mobile == user.mobile).first():
        raise HTTPException(status_code=400, detail="Mobile number already registered")


    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password(user.password),
        mobile=user.mobile,
        age=user.age,
        gender=user.gender,
        role=user.role or "user",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return True



def update_user_profile(db: Session, user_id: int, data: UserUpdateProfile):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Only update name fields
    if data.first_name:
        user.first_name = data.first_name
    if data.last_name:
        user.last_name = data.last_name
    if data.mobile:
        user.mobile = data.mobile
        


    # Password update logic
    if data.new_password or data.confirm_password:
        if not data.new_password or not data.confirm_password:
            raise HTTPException(status_code=400, detail="Both new_password and confirm_password are required")
        if data.new_password != data.confirm_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")
        user.password = hash_password(data.new_password)

    user.updated_at = datetime.now()
    db.commit()
    db.refresh(user)
    return user


def admin_update_user(db: Session, user_id: int, data: AdminUpdateUser):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.first_name is not None:
        user.first_name = data.first_name
    if data.last_name is not None:
        user.last_name = data.last_name
    if data.email is not None:
        user.email = data.email
    if data.mobile is not None:
        user.mobile = data.mobile
    if data.age is not None:
        user.age = data.age
    if data.gender is not None:
        user.gender = data.gender
    if data.role is not None:
        user.role = data.role

    # ✅ Only hash and update password if it's non-empty
    if data.password is not None and data.password.strip() != "":
        user.password = hash_password(data.password)

    user.updated_at = datetime.now()
    db.commit()
    db.refresh(user)
    return user








# def create_user(db: Session, user: UserCreate):
#     existing_user = db.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
    

    


# # def create_user(db: Session, user: UserCreate):
# #     # ✅ Check for existing email
# #     existing_email = db.query(User).filter(User.email == user.email).first()
# #     if existing_email:
# #         raise HTTPException(status_code=400, detail="Email already registered")

# #     # ✅ Check for existing mobile
# #     existing_mobile = db.query(User).filter(User.mobile == user.mobile).first()
# #     if existing_mobile:
# #         raise HTTPException(status_code=400, detail="Mobile number already registered")