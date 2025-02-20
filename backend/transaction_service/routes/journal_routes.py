from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.schemas import JournalCreate, JournalResponse
from database import crud

router = APIRouter()

@router.post("/", response_model=JournalResponse)
def create_journal_entry(journal_entry: JournalCreate, db: Session = Depends(get_db)):
    return crud.create_journal_entry(db, journal_entry)
