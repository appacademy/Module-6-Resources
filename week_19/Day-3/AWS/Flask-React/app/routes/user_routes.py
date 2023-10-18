from flask import Blueprint
from ..models import User


users = Blueprint("users", __name__)
# print("in user bp", __name__)


@users.route("/all")
def get_all_users():
    all_users = [user.to_dict_no_posts() for user in  User.query.all()]
    print(all_users)
    return { "users": all_users }