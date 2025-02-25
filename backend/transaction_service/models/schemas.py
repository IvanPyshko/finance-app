from pydantic import BaseModel
from datetime import date
from typing import Optional

class AcctBase(BaseModel):
    name: str

class AcctResponse(AcctBase):
    id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class JournalCreate(BaseModel):
    date: date
    acct_id: int
    dom_amount: float
    for_amount: float
    currency: str
    exch_rate: float
    category_id: int
    #comment_id: int | None = None  # Можем передавать NULL при создании

class JournalResponse(BaseModel):
    id: int
    date: date
    acct_id: int
    dom_amount: float
    for_amount: float
    currency: str
    exch_rate: float
    category_id: int

    class Config:
        from_attributes = True
        
class CommentBase(BaseModel):
    text: str  # Текст комментария (обязательное поле)
    #journal_id: int

class CommentResponse(CommentBase):
    id: int  # ID комментария в БД

    class Config:
        from_attributes = True