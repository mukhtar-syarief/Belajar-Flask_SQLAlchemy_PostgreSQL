from flask import session
from src.models.comments import Comments
from src.models.models import s
from src.models.users import Users
from src.models.articles import Articles

#Mencari Komentar Berdasarkan Artikel
def find_comment_by_article_id(article_id):
    comments = s.query(Comments).filter(Comments.article_id == article_id).all()
    return comments

#Membuat Komentar
def created_comments(id, komentar):
    user = s.query(Users).filter(Users.id == session["_user_id"]).first()
    article = s.query(Articles).filter(Articles.id == id).first()
    comment = Comments(komentar = f"{komentar}", user = user, article = article)
    s.add(comment)
    s.commit()
    return True