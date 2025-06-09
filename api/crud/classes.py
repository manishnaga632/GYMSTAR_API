from sqlalchemy.orm import Session
from api.database.models.classes import ClassModel
from api.database.schemas.classes import ClassCreate

# ✅ Create
def create_class(db: Session, class_data: ClassCreate):
    new_class = ClassModel(**class_data.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

# ✅ Read all
def get_all_classes(db: Session):
    return db.query(ClassModel).all()

# ✅ Read by ID
def get_class_by_id(db: Session, class_id: int):
    return db.query(ClassModel).filter(ClassModel.id == class_id).first()

# ✅ Update
def update_class(db: Session, class_id: int, class_data: ClassCreate):
    db_class = db.query(ClassModel).filter(ClassModel.id == class_id).first()
    if db_class:
        for key, value in class_data.dict().items():
            setattr(db_class, key, value)
        db.commit()
        db.refresh(db_class)
        return db_class
    return None

# ✅ Delete
def delete_class(db: Session, class_id: int):
    db_class = db.query(ClassModel).filter(ClassModel.id == class_id).first()
    if db_class:
        db.delete(db_class)
        db.commit()
        return True
    return False
