from flask import Blueprint, render_template
from flask_login import current_user

home_api = Blueprint("home", __name__)

@home_api.route("/")
def home():
    return render_template ('home/index.html', user = current_user)