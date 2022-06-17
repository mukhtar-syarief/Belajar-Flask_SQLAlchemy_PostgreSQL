from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.orm import relationship
from src.models.config import db


class Tags(db):
    __tablename__ = "tags"
    id = Column(Integer, primary_key = True)
    nama = Column(VARCHAR[20])
    article = relationship("ArticleTag", back_populates = "tags", cascade = "all, delete")
