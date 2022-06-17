from flask import Blueprint, render_template
from flask_login import login_required
from src.controller.categories import find_categorie_by_name, all_categories

categorie = Blueprint("categorie", __name__)

@categorie.route("/article/<categories>")
@login_required
def post_categorie(categories):
    categorie_artikels = find_categorie_by_name(categories)
    all_categorie = all_categories()
    return render_template("post/post_categorie.html", categories = all_categorie, articles = categorie_artikels.articles)
