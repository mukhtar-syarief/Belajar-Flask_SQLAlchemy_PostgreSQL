from flask import Flask
from flask_login import LoginManager

from src.controller.user import find_user_by_id

from src.blueprint.home import home_api
from src.blueprint.login import login_api
from src.blueprint.signup import signup_api
from src.blueprint.article import article
from src.blueprint.article_detail import detail
from src.blueprint.comments import comments
from src.blueprint.new_article import new_articles
from src.blueprint.article_edit import article_edit
from src.blueprint.delete_article import delete_article
from src.blueprint.article_categorie import categorie
from src.blueprint.user_api import user
from src.blueprint.logout import logout

app = Flask(__name__, template_folder = "views/template", static_folder = "views/static")
app.config["SECRET_KEY"] = "MencintaiDalamSepi"



app.register_blueprint(home_api)
app.register_blueprint(login_api)
app.register_blueprint(signup_api)
app.register_blueprint(article)
app.register_blueprint(detail)
app.register_blueprint(new_articles)
app.register_blueprint(article_edit)
app.register_blueprint(comments)
app.register_blueprint(delete_article)
app.register_blueprint(categorie)
app.register_blueprint(user)
app.register_blueprint(logout)

login_manager = LoginManager()
login_manager.login_view = "login.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return find_user_by_id(id)

if __name__ == "__main__":
    app.run(debug=True)