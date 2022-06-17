from flask import Blueprint, redirect, render_template, request
from src.controller.article import create_article
from src.controller.categories import all_categories
from flask_login import login_required

new_articles = Blueprint("new_articles", __name__)

@new_articles.route("/new", methods=['POST', 'GET'])
@login_required
def new_article():
    if request.method == "GET":
        all_categorie = all_categories()
        return render_template("post/post.html", categories = all_categorie)
    else:
        categorie_id = request.form.get('categorie')
        judul = request.form.get("judul")
        konten = request.form.get("konten")
        tags = request.form.get("tag")
        create_article(judul, konten, tags, categorie_id)
        return redirect("/article")
