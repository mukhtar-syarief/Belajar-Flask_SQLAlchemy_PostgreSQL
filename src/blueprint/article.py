from flask import Blueprint, render_template
from src.controller.article import all_article
from src.controller.categories import all_categories
from flask_login import login_required

article = Blueprint("article", __name__)

@article.route("/article")
@login_required
def post():
    list_article = all_article()
    all_categorie = all_categories()
    return render_template('post/index.html', list_artikels = list_article, categories = all_categorie)