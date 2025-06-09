from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database.schemas.static_manager import StaticCreate, StaticUpdate, StaticOut
from api.crud import static_manager
from api.database.connection import get_db

router = APIRouter()

@router.get("/aal_static", response_model=List[StaticOut])
def read_static_pages(db: Session = Depends(get_db)):
    return static_manager.get_all_static(db)

@router.get("/get_static_by_id{static_id}", response_model=StaticOut)
def read_static(static_id: int, db: Session = Depends(get_db)):
    db_static = static_manager.get_static_by_id(db, static_id)
    if not db_static:
        raise HTTPException(status_code=404, detail="Static content not found")
    return db_static

@router.post("/add_static", response_model=StaticOut)
def create_static(static_data: StaticCreate, db: Session = Depends(get_db)):
    return static_manager.create_static(db, static_data)

@router.put("/update_static{static_id}", response_model=StaticOut)
def update_static(static_id: int, static_data: StaticUpdate, db: Session = Depends(get_db)):
    return static_manager.update_static(db, static_id, static_data)

@router.delete("/delete_static{static_id}")
def delete_static(static_id: int, db: Session = Depends(get_db)):
    result = static_manager.delete_static(db, static_id)
    if not result:
        raise HTTPException(status_code=404, detail="Static content not found")
    return {"message": "Static content deleted successfully"}
