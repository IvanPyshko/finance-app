from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Acct(Base):
    __tablename__ = "acct"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    journal_entries = relationship("Journal", back_populates="acct_rel")
