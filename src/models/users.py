from sqlalchemy import Column, DateTime, Integer, Text, func
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from src.models.config import db
from src.models.comments import Comments
from src.models.articles import Articles

class Users(db, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    nama = Column(Text)
    email = Column(Text, unique = True)
    password = Column(Text)
    created_at = Column(DateTime, default = func.now())
    articles = relationship("Articles", back_populates = "user", cascade = "all, delete")
    komentar = relationship("Comments", back_populates = "user", cascade = "all, delete")