from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database.schemas.trainers import TrainerCreate, TrainerUpdate, TrainerOut
from api.crud import trainers
from api.database.connection import get_db

router = APIRouter()

@router.get("/all_trainers", response_model=List[TrainerOut])
def read_trainers(db: Session = Depends(get_db)):
    return trainers.get_all_trainers(db)

@router.get("/get_trainer_by_id/{trainer_id}", response_model=TrainerOut)
def read_trainer(trainer_id: int, db: Session = Depends(get_db)):
    trainer = trainers.get_trainer_by_id(db, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer

@router.post("/add", response_model=TrainerOut)
def create_trainer(trainer_data: TrainerCreate, db: Session = Depends(get_db)):
    return trainers.create_trainer(db, trainer_data)

@router.put("/update/{trainer_id}", response_model=TrainerOut)
def update_trainer(trainer_id: int, trainer_data: TrainerUpdate, db: Session = Depends(get_db)):
    return trainers.update_trainer(db, trainer_id, trainer_data)

@router.delete("/delete/{trainer_id}")
def delete_trainer(trainer_id: int, db: Session = Depends(get_db)):
    result = trainers.delete_trainer(db, trainer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return {"message": "Trainer deleted successfully"}
