from flask import Blueprint

users = Blueprint("users", __name__)

# print("inside the users bp", __name__)


@users.route("/all")
def get_all_users():
    return "<h1>Look at all the lovely users...</h1>"