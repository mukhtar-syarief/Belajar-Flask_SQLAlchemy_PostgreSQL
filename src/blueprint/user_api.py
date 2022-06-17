from flask import Blueprint, render_template
from flask_login import login_required
from src.controller.user import find_user_by_nama


user = Blueprint("user", __name__)

@user.route("/<user_detail>")
@login_required
def user_detail(user_detail):
    user = find_user_by_nama(user_detail)
    return render_template("user/user.html", user = user)
