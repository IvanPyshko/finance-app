from sqlalchemy import Column, Integer, String
from database.db import Base
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(256), nullable=False)  # Текст комментария

    journal_entries = relationship("Journal", back_populates="comment")
