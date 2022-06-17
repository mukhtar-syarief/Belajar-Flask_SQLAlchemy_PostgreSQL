from flask import  Blueprint, render_template
from src.controller.article import find_article_by_id
from src.controller.comment import find_comment_by_article_id
from flask_login import login_required

detail = Blueprint("detail", __name__)

@detail.route("/article_detail/<id>")
@login_required
def post_detail(id):
    article = find_article_by_id(id)
    comments = find_comment_by_article_id(id)
    return render_template("post/post_detail.html", article = article, comments = comments)