from flask import Blueprint, redirect, render_template, request
from src.controller.article import change_article, find_article_by_id
from flask_login import login_required

article_edit = Blueprint("article_edit", __name__)

@article_edit.route("/article/<id>/edit", methods=["POST", "GET"])
@login_required
def edit_article(id):
    if request.method == "GET":
        article = find_article_by_id(id)
        return render_template("post/edit.html", article = article)
    else:
        judul = request.form.get("judul")
        konten = request.form.get("konten")
        change_article(id, judul, konten)
        return redirect(f"/article_detail/{id}")

