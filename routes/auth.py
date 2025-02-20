import flask as flask
import controllers.auth as auth

auth_blp = flask.Blueprint("auth", __name__)

@auth_blp.route("/login", methods=["POST"])
def login():
    return auth._LoginController().login()

@auth_blp.route("/user", methods=["POST"])
def add_user():
    return auth._UserController().create()

@auth_blp.route("/user", methods=["GET"])
def get_all_user():
    return auth._UserController().get_all()

@auth_blp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return auth._UserController().get(user_id)

@auth_blp.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return auth._UserController().update(user_id)

@auth_blp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return auth._UserController().delete(user_id)
