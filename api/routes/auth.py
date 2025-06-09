
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from api.database.schemas.user import UserLogin
from api.database.connection import get_db
from api.security import verify_password
from api.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from api.database.models.user import User

router = APIRouter()

@router.post("/login", response_model=dict)
async def login(
    user_data: UserLogin, 
    db: Session = Depends(get_db)
):
    # Find user by email
    user = db.query(User).filter(User.email == user_data.email).first()
    
    # Verify credentials
    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create token with user data
    access_token = create_access_token(
        data={
            "sub": user.email,
            "user_id": user.id,
            "role": user.role
        },
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_info": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    }
