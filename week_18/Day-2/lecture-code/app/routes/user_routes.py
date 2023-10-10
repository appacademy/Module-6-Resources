from flask import Blueprint



users = Blueprint("users", __name__)
print("in user bp", __name__)


@users.route("/all")
def get_all_users():
    return "<h2>One day users will be here...</h2>"