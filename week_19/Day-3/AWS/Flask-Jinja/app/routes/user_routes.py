from flask import Blueprint


users = Blueprint('users', __name__)

# print(__name__, "inside the user routes")


@users.route("/all")
def get_all_users():
    return "<h2>Users will one day maybe be here</h2>"