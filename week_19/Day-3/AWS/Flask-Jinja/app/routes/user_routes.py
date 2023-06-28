from flask import Blueprint
from ..models import User

user_routes = Blueprint("names", __name__)


@user_routes.route("/all")
def users():
  response = [user.to_dict() for user in User.query.all()]
  print(response)
  return "<h1>No users yet!</h1>"