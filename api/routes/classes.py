from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.schemas.classes import ClassCreate, ClassOut
from api.crud import classes as crud_classes
from api.database.connection import get_db

router = APIRouter()

# ✅ Create class
@router.post("/add", response_model=ClassOut)
def add_class(class_data: ClassCreate, db: Session = Depends(get_db)):
    return crud_classes.create_class(db, class_data)

# ✅ Get all classes
@router.get("/all", response_model=list[ClassOut])
def get_all_classes(db: Session = Depends(get_db)):
    return crud_classes.get_all_classes(db)

# ✅ Get class by ID
@router.get("/{class_id}", response_model=ClassOut)
def get_class_by_id(class_id: int, db: Session = Depends(get_db)):
    db_class = crud_classes.get_class_by_id(db, class_id)
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class

# ✅ Update class
@router.put("/update/{class_id}", response_model=ClassOut)
def update_class(class_id: int, class_data: ClassCreate, db: Session = Depends(get_db)):
    db_class = crud_classes.update_class(db, class_id, class_data)
    if not db_class:
        raise HTTPException(status_code=404, detail="Class not found")
    return db_class

# ✅ Delete class
@router.delete("/delete/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    success = crud_classes.delete_class(db, class_id)
    if not success:
        raise HTTPException(status_code=404, detail="Class not found")
    return {"message": "Class deleted successfully"}
