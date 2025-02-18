import flask as flask
import controllers.auth as auth

auth_blp = flask.Blueprint("auth", __name__)

@auth_blp.route("/register", methods=["POST"])
def register():
    return auth._RegisterController().register()

@auth_blp.route("/login", methods=["POST"])
def login():
    return auth._LoginController().login()

