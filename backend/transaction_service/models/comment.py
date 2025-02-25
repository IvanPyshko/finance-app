from sqlalchemy import Column, Integer, String
from database.db import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(256), nullable=False)