from flask import Blueprint


users = Blueprint("users", __name__)


# "/users"
# @users.route("")

# "/users/"
# @users.route("/")

# "/users/all"
@users.route("/all")
def get_all_users():
    # users = Users.query.all()
    return "<h2>Them be users here...</h2>"