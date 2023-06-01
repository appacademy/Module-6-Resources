from flask import Blueprint
from ..models import User

users = Blueprint("users", __name__)


# "/users"
# @users.route("")

# "/users/"
# @users.route("/")

# "/users/all"
@users.route("/all")
def get_all_users():
    response = [user.to_dict() for user in User.query.all()]
    # print(response)
    return {"users": response }