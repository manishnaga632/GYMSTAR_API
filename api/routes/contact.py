
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.connection import get_db
from api.database.schemas.contact import ContactCreate, ContactResponse
from api.crud import contact as crud_contact

router = APIRouter()

@router.post("/add", response_model=ContactResponse)
def create_contact(form: ContactCreate, db: Session = Depends(get_db)):
    return crud_contact.create_contact(db, form)

@router.get("/all", response_model=List[ContactResponse])
def get_all_contacts(db: Session = Depends(get_db)):
    return crud_contact.get_all_contacts(db)



@router.patch("/seen/{contact_id}", response_model=ContactResponse)
def mark_contact_as_seen(contact_id: int, db: Session = Depends(get_db)):
    contact = crud_contact.mark_as_seen(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.delete("/delete/{contact_id}", response_model=ContactResponse)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud_contact.delete_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
