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

class JournalBase(BaseModel):
    date: date
    acct: int
    dom_amount: float
    for_amount: float
    currency: str
    exch_rate: float
    category_id: int
    comment_id: Optional[int] = None

class JournalCreate(JournalBase):
    pass

class JournalResponse(JournalBase):
    id: int

    class Config:
        from_attributes = True
        
class CommentBase(BaseModel):
    text: str  # Текст комментария (обязательное поле)

class CommentResponse(CommentBase):
    id: int  # ID комментария в БД

    class Config:
        from_attributes = True