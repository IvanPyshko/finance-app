from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.schemas import CategoryBase, CategoryResponse
from database import crud

router = APIRouter()

@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryBase, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)
