from flask import session
from src.models.categorie_articele import CategorieArticle
from src.models.categories import Categories
from src.models.articles import Articles
from src.models.users import Users
from src.models.tags import Tags
from src.models.artikel_tag_assosiation import ArticleTag
from src.controller.categories import find_categorie_by_id
from src.models.models import s

#Mencari Semua Artikel
def all_article():
    all_article = s.query(Articles).all()
    return all_article

def find_article_by_id(id):
    article = s.query(Articles).filter(Articles.id == id).first()
    return article

def find_artikel_by_user_id(user_id):
    articles = s.query(Articles).filter(Articles.user_id == user_id)
    return articles

def create_article(judul, konten, tags, categorie_id):
    categorie = s.query(Categories).filter(Categories.id == categorie_id).first()
    user = s.query(Users).filter(Users.id == session["_user_id"]).first()
    new_article = Articles(judul = f"{judul}", konten = f"{konten}", user = user)
    s.add(new_article)
    new_tag = Tags(nama = f"{tags}")
    s.add(new_tag)
    article_tag = ArticleTag(article = new_article, tags = new_tag)
    s.add(article_tag)
    categorie_article = CategorieArticle(categories = categorie, articles = new_article)
    s.add(categorie_article)
    s.commit()

def change_article(id, judul, konten):
    article = s.query(Articles).filter(Articles.id == id).first()
    article.judul = judul
    article.konten = konten
    s.commit()

def deleting_article(id):
    article = s.query(Articles).filter(Articles.id == id).first()
    s.delete(article) 
    s.commit()
    return "Berhasil didelete"