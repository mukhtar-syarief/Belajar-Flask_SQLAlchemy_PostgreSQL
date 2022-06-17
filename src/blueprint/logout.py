from flask import Blueprint, redirect, session
from flask_login import logout_user
from flask_login import login_required

logout = Blueprint("logout", __name__)

@logout.route("/logout")
@login_required
def user_logout():
    logout_user()
    if "email" in session:
        session.pop("user_id")
        session.pop("nama")
        session.pop("email")
        return redirect('/')
    else:
        return redirect('/')
