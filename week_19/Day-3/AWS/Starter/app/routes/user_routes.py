from flask import Blueprint


users = Blueprint("users", __name__)
# print(__name__)


@users.route("/all")
def get_all_users():
    return "<h1>Users would be here...</h1>"