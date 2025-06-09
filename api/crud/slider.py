from sqlalchemy.orm import Session
from api.database.models.slider import Slider
from api.database.schemas.slider import SliderCreate, SliderUpdate

def get_all_sliders(db: Session):
    return db.query(Slider).all()

def get_slider_by_id(db: Session, slider_id: int):
    return db.query(Slider).filter(Slider.id == slider_id).first()

def create_slider(db: Session, slider: SliderCreate):
    db_slider = Slider(**slider.dict())
    db.add(db_slider)
    db.commit()
    db.refresh(db_slider)
    return db_slider

def update_slider(db: Session, slider_id: int, slider: SliderUpdate):
    db_slider = db.query(Slider).filter(Slider.id == slider_id).first()
    if db_slider:
        for key, value in slider.dict(exclude_unset=True).items():
            setattr(db_slider, key, value)
        db.commit()
        db.refresh(db_slider)
    return db_slider

def delete_slider(db: Session, slider_id: int):
    db_slider = db.query(Slider).filter(Slider.id == slider_id).first()
    if db_slider:
        db.delete(db_slider)
        db.commit()
    return db_slider
