from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.schemas import AcctBase, AcctResponse
from database import crud

router = APIRouter()

@router.post("/", response_model=AcctResponse)
def create_acct(acct: AcctBase, db: Session = Depends(get_db)):
    return crud.create_acct(db, acct)

@router.get("/", response_model=list[AcctResponse])
def get_accts(db: Session = Depends(get_db)):
    return crud.get_accts(db)
