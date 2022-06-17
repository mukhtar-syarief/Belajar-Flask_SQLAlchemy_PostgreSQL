from flask import Blueprint, request, render_template, redirect, session
from src.controller.comment import created_comments
from flask_login import login_required

comments = Blueprint("comments", __name__)

@comments.route("/article/<id>/comments", methods = ["POST", "GET"])
@login_required
def create_comment(id):
    if request.method == "GET":
        return render_template('post/post_komen.html',id = id)   
    else:
        komentar = request.form.get('comment')
        created_comments(id, komentar)
        return redirect(f'/article_detail/{id}')