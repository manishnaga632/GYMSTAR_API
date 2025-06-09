from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import Query
from typing import Optional
from api.database.schemas.user import UserCreate, UserOut, UserUpdateProfile, AdminUpdateUser
from api.database.connection import get_db
from api.crud import user as user_crud
from api.database.models.user import User
from api.token import get_current_user, get_current_admin_user

router = APIRouter()


# Anyone can register
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

# ✅ Only admin can get all users
@router.get("/all_users", response_model=list[UserOut])
def get_all_users_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return user_crud.get_all_users(db)

# ✅ Only admin can view all users
@router.get("/get_user_by_id/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    user = user_crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user



# ✅ Only admin can delete users
@router.delete("/delete_users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    if not user_crud.delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}

# ✅ Logged-in user can update their own profile
@router.put("/profile_update", response_model=UserOut)
def update_profile(data: UserUpdateProfile, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_crud.update_user_profile(db, current_user.id, data)

# ✅ Admin can update any user
@router.put("/admin_update/{user_id}", response_model=UserOut)
def admin_update_user(user_id: int, data: AdminUpdateUser, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return user_crud.admin_update_user(db, user_id, data)


# ✅ Logged-in user can get their own profile
@router.get("/profile", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/check-unique")
def check_unique(
    db: Session = Depends(get_db),
    email: Optional[str] = Query(None),
    mobile: Optional[str] = Query(None)
):
    if not email and not mobile:
        raise HTTPException(status_code=400, detail="Email or mobile is required")

    if email and db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=409, detail="Email already registered")

    if mobile and db.query(User).filter(User.mobile == mobile).first():
        raise HTTPException(status_code=409, detail="Mobile number already registered")

    return {"detail": "Available"}
