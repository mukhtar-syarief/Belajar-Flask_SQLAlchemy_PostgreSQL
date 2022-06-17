from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.config import db

class Categories(db):
    __tablename__ = "categories"
    id = Column(Integer, primary_key = True)
    categories = Column(String)
    articles = relationship("CategorieArticle", back_populates = "categories")