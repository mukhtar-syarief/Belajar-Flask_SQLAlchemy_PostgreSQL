from sqlalchemy import VARCHAR, Column, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import relationship
from src.models.config import db
from src.models.categorie_articele import CategorieArticle
from src.models.artikel_tag_assosiation import ArticleTag


class Articles(db):
    __tablename__ = "articles"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"))
    judul = Column(VARCHAR[50])
    konten = Column(Text)
    created_at = Column(DateTime, default = func.now())
    last_modified = Column(DateTime, default = func.now(), onupdate=func.now())
    user = relationship("Users", back_populates = "articles")
    komentar = relationship("Comments", back_populates = "article", cascade = "all, delete")
    tags = relationship("ArticleTag", back_populates = "article", cascade = "all, delete")
    categories = relationship("CategorieArticle", back_populates = "articles", cascade = "all, delete")