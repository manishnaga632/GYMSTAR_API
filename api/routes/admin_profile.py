from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.schemas.admin_profile import (
    AdminProfileCreate, AdminProfileUpdate, AdminProfileOut
)
from api.crud import admin_profile
from api.database.connection import get_db

router = APIRouter()

@router.get("/all", response_model=List[AdminProfileOut])
def read_all_profiles(db: Session = Depends(get_db)):
    return admin_profile.get_all_profiles(db)

@router.get("/{profile_id}", response_model=AdminProfileOut)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = admin_profile.get_profile_by_id(db, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.post("/add", response_model=AdminProfileOut)
def create_admin_profile(profile: AdminProfileCreate, db: Session = Depends(get_db)):
    return admin_profile.create_profile(db, profile)

@router.put("/update/{profile_id}", response_model=AdminProfileOut)
def update_admin_profile(profile_id: int, profile: AdminProfileUpdate, db: Session = Depends(get_db)):
    return admin_profile.update_profile(db, profile_id, profile)

@router.delete("/delete/{profile_id}")
def delete_admin_profile(profile_id: int, db: Session = Depends(get_db)):
    result = admin_profile.delete_profile(db, profile_id)
    if not result:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Admin profile deleted successfully"}
