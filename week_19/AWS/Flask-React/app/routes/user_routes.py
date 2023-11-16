from flask import Blueprint
from ..models import User

users = Blueprint("users", __name__)
# print("in the user bp", __name__)


@users.route("/all")
def get_all_users():
    response = [user.to_dict_no_posts() for user in User.query.all()]
    print(response)
    return {"users": response}


