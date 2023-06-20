from flask import Blueprint


user_routes = Blueprint("names", __name__)


@user_routes.route("")
def users():
  return "<h1>No users yet!</h1>"