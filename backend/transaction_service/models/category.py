from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    journal_entries = relationship("Journal", back_populates="category")
