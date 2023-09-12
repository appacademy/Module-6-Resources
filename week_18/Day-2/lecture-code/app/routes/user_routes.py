from flask import Blueprint

users = Blueprint("users", __name__, url_prefix="/users")
# print("inside the users bp", __name__)


@users.route("all")
def get_all_users():
    return "<h1>All users would be here...</h1>"