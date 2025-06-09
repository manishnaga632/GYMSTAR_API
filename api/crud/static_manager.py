from sqlalchemy.orm import Session
from api.database.models.static_manager import StaticManager
from api.database.schemas.static_manager import StaticCreate, StaticUpdate

def get_all_static(db: Session):
    return db.query(StaticManager).all()

def get_static_by_id(db: Session, static_id: int):
    return db.query(StaticManager).filter(StaticManager.id == static_id).first()

def create_static(db: Session, static: StaticCreate):
    db_static = StaticManager(**static.dict())
    db.add(db_static)
    db.commit()
    db.refresh(db_static)
    return db_static

def update_static(db: Session, static_id: int, static: StaticUpdate):
    db_static = db.query(StaticManager).filter(StaticManager.id == static_id).first()
    if db_static:
        for key, value in static.dict(exclude_unset=True).items():
            setattr(db_static, key, value)
        db.commit()
        db.refresh(db_static)
    return db_static

def delete_static(db: Session, static_id: int):
    db_static = db.query(StaticManager).filter(StaticManager.id == static_id).first()
    if db_static:
        db.delete(db_static)
        db.commit()
    return db_static
