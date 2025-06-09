from sqlalchemy.orm import Session
from api.database.models.admin_profile import AdminProfile
from api.database.schemas.admin_profile import AdminProfileCreate, AdminProfileUpdate

def get_all_profiles(db: Session):
    return db.query(AdminProfile).all()

def get_profile_by_id(db: Session, profile_id: int):
    return db.query(AdminProfile).filter(AdminProfile.id == profile_id).first()

def create_profile(db: Session, profile: AdminProfileCreate):
    db_profile = AdminProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile_id: int, profile: AdminProfileUpdate):
    db_profile = db.query(AdminProfile).filter(AdminProfile.id == profile_id).first()
    if db_profile:
        for key, value in profile.dict(exclude_unset=True).items():
            setattr(db_profile, key, value)
        db.commit()
        db.refresh(db_profile)
    return db_profile

def delete_profile(db: Session, profile_id: int):
    db_profile = db.query(AdminProfile).filter(AdminProfile.id == profile_id).first()
    if db_profile:
        db.delete(db_profile)
        db.commit()
    return db_profile
