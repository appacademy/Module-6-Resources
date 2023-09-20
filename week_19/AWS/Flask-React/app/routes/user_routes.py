from flask import Blueprint
from ..models import db, User

users = Blueprint("users", __name__, url_prefix="/users")
# print("inside the users bp", __name__)


@users.route("/all")
def get_all_users():
    response = [user.to_dict() for user in User.query.all()]
    print(response)
    return {"users": response }