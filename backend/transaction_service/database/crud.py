from sqlalchemy.orm import Session
from models.journal import Journal
from models.acct import Acct
from models.category import Category
from models.comment import Comment
from models.schemas import JournalCreate, AcctBase, CategoryBase, CommentBase
from fastapi import HTTPException

def create_journal_entry(db: Session, journal_entry: JournalCreate):
    new_entry = Journal(
     date=journal_entry.date,
     acct_id=journal_entry.acct_id,
     dom_amount=journal_entry.dom_amount,
     for_amount=journal_entry.for_amount,
     currency=journal_entry.currency,
     exch_rate=journal_entry.exch_rate,
     category_id=journal_entry.category_id,
    )
        #comment_id=None  # Комментарий добавится позже

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def create_acct(db: Session, acct_data: AcctBase):
    db_acct = Acct(**acct_data.dict())
    db.add(db_acct)
    db.commit()
    db.refresh(db_acct)
    return db_acct

def create_category(db: Session, category_data: CategoryBase):
    db_category = Category(**category_data.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_comment(db: Session, comment: CommentBase):
    # Создаем комментарий
    new_comment = Comment(text=comment.text)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_accts(db: Session):
    return db.query(Acct).all()

def get_categories(db: Session):
    return db.query(Category).all()

def get_comments(db: Session):
    return db.query(Comment).all()
