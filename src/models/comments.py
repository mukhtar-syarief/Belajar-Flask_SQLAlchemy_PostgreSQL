from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime, func
from sqlalchemy.orm import relationship
from src.models.config import db


class Comments(db):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"))
    article_id = Column(Integer, ForeignKey("articles.id", ondelete = "CASCADE"))
    komentar = Column(Text)
    created_at = Column(DateTime, default = func.now())
    user = relationship("Users", back_populates = "komentar", cascade="all, delete")
    article = relationship("Articles", back_populates = "komentar", cascade = "all, delete")