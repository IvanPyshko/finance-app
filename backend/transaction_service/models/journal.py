from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.db import Base

class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    acct = Column(Integer, ForeignKey("acct.id"), nullable=False)
    dom_amount = Column(Float, nullable=False)
    for_amount = Column(Float, nullable=False)
    currency = Column(String(3), nullable=False)
    exch_rate = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    acct_rel = relationship("Acct", back_populates="journal_entries")
    category = relationship("Category", back_populates="journal_entries")
    comment = relationship("Comment", back_populates="journal_entry", uselist=False)
