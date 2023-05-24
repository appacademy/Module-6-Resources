from flask import Blueprint


users = Blueprint("users", __name__)


print(__name__, "inside the users route")



@users.route("/all")
def all_users():
    return "<h2>One day there might be users here...</h2>"