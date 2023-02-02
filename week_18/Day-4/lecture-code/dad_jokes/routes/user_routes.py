from flask import Blueprint

user_routes = Blueprint("user", __name__)


@user_routes.route('/')
def get_users():
    return "<h3>One day there might be users here...</h3>"