from flask import Blueprint
from ..models import User

user_routes = Blueprint("names", __name__)


@user_routes.route("/all")
def users():
  response = [user.to_dict_no_post() for user in User.query.all()]
  print(response)
  return {"users": response }