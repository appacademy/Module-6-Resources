from flask import Blueprint

users = Blueprint("users", __name__)

# print("inside users BP", __name__)


@users.route("/")
def user_stuff():
    return "<h2>Users Stuff here!</h2>"