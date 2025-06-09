from sqlalchemy.orm import Session
from api.database.models.trainers import Trainer
from api.database.schemas.trainers import TrainerCreate, TrainerUpdate

def get_all_trainers(db: Session):
    return db.query(Trainer).all()

def get_trainer_by_id(db: Session, trainer_id: int):
    return db.query(Trainer).filter(Trainer.id == trainer_id).first()

def create_trainer(db: Session, trainer: TrainerCreate):
    db_trainer = Trainer(**trainer.dict())
    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer

def update_trainer(db: Session, trainer_id: int, trainer: TrainerUpdate):
    db_trainer = db.query(Trainer).filter(Trainer.id == trainer_id).first()
    if db_trainer:
        for key, value in trainer.dict(exclude_unset=True).items():
            setattr(db_trainer, key, value)
        db.commit()
        db.refresh(db_trainer)
    return db_trainer

def delete_trainer(db: Session, trainer_id: int):
    db_trainer = db.query(Trainer).filter(Trainer.id == trainer_id).first()
    if db_trainer:
        db.delete(db_trainer)
        db.commit()
    return db_trainer
