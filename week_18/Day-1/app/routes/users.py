from flask import Blueprint, render_template
from app.posts import users

user_routes = Blueprint("user_routes", __name__, url_prefix="/users")

@user_routes.route("/<int:id>")
def one_user(id):
    return render_template("user.html", users=users, id=id )

