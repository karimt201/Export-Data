import flask as flask
import controllers.auth as auth

auth_blp = flask.Blueprint("auth", __name__)

@auth_blp.route("/login", methods=["POST"])
def login():
    return auth.LoginController().login()

@auth_blp.route("/register", methods=["POST"])
def add_user():
    return auth.RegisterController(flask.request).register()

@auth_blp.route("/users", methods=["GET"])
def get_all_user():
    return auth.ReadAllUserController().get_all()

@auth_blp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return auth.ReadUserController().get(user_id)

@auth_blp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return auth.UpdateUserController().update(user_id)

@auth_blp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return auth.DeleteUserController().delete(user_id)
