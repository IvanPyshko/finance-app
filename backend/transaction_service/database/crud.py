from sqlalchemy.orm import Session
from models.journal import Journal
from models.acct import Acct
from models.category import Category
from models.schemas import JournalCreate, AcctBase, CategoryBase

def create_journal_entry(db: Session, journal_data: JournalCreate):
    db_entry = Journal(**journal_data.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

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

def get_accts(db: Session):
    return db.query(Acct).all()

def get_categories(db: Session):
    return db.query(Category).all()
