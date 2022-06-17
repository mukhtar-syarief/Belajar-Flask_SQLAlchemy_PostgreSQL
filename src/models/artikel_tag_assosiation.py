from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.models.config import db

class ArticleTag(db):
    __tablename__ = "article_tag_assosiation"
    id = Column(Integer, primary_key = True)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete = "CASCADE"))
    tag_id = Column(Integer, ForeignKey("tags.id", ondelete = "CASCADE"))
    article = relationship("Articles", back_populates = "tags", cascade = "all, delete")
    tags = relationship("Tags", back_populates = "article", cascade = "all, delete")
    
    def __repr__(self):
        return f"ArticleTag(id = {self.id}, article_id = {self.article_id})"

