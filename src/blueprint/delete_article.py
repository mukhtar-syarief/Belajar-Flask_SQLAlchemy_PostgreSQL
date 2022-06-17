from flask import Blueprint, redirect
from src.controller.article import deleting_article
from flask_login import login_required

delete_article = Blueprint("delete_article", __name__)

@delete_article.route("/article/<id>/delete")
@login_required
def destroy_article(id):
    deleting_article(id)
    return redirect("/article")