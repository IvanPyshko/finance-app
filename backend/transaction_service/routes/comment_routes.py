from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.schemas import CommentBase, CommentResponse
from database import crud

router = APIRouter()

@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentBase, db: Session = Depends(get_db)):
    return crud.create_comment(db, comment)

@router.get("/", response_model=list[CommentResponse])
def get_comments(db: Session = Depends(get_db)):
    return crud.get_comments(db)
