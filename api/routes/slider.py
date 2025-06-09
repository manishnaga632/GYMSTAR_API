from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database.schemas.slider import SliderCreate, SliderUpdate, SliderOut
from api.crud import slider  # crud file ka import
from api.database.connection import get_db

router = APIRouter()

@router.get("/all", response_model=List[SliderOut])
def read_sliders(db: Session = Depends(get_db)):
    return slider.get_all_sliders(db)

@router.get("/get/{slider_id}", response_model=SliderOut)
def read_slider(slider_id: int, db: Session = Depends(get_db)):
    db_slider = slider.get_slider_by_id(db, slider_id)
    if not db_slider:
        raise HTTPException(status_code=404, detail="Slider not found")
    return db_slider

@router.post("/add", response_model=SliderOut)
def create_slider(slider_data: SliderCreate, db: Session = Depends(get_db)):
    return slider.create_slider(db, slider_data)

@router.put("/update/{slider_id}", response_model=SliderOut)
def update_slider(slider_id: int, slider_data: SliderUpdate, db: Session = Depends(get_db)):
    return slider.update_slider(db, slider_id, slider_data)

@router.delete("/delete/{slider_id}")
def delete_slider(slider_id: int, db: Session = Depends(get_db)):
    result = slider.delete_slider(db, slider_id)
    if not result:
        raise HTTPException(status_code=404, detail="Slider not found")
    return {"message": "Slider deleted successfully"}
