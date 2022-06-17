from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.models.config import db

class CategorieArticle(db):
    __tablename__ = "article_categorie"
    id = Column(Integer, primary_key = True)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"))
    categorie_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    articles = relationship("Articles", back_populates = "categories", cascade = "all, delete")
    categories = relationship("Categories", back_populates = "articles")

    def __repr__(self):
        return f"CategorieArticle(id = {self.id}, article_id = {self.article_id}, categorie_id = {self.categorie_id})"
