from flask import Blueprint

users = Blueprint("users", __name__)
# print("in the user bp", __name__)


@users.route("/all")
def get_all_users():
    # 
    return "<h2>Users will be here...</h2>"



